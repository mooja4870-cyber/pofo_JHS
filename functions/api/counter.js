export async function onRequest(context) {
    const { request, env } = context;
    const url = new URL(request.url);
    const action = url.searchParams.get('action');
    const appId = url.searchParams.get('appId');
    const isAdmin = url.searchParams.get('isAdmin') === 'true';

    const headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    };

    try {
        // KV에서 현재 방문자 수 가져오기
        let totalVisitors = parseInt(await env.POFO_COUNTER.get('total_visitors')) || 0;
        let totalVisitorsExternal = parseInt(await env.POFO_COUNTER.get('total_visitors_external')) || 0;
        let totalVisitorsAdmin = parseInt(await env.POFO_COUNTER.get('total_visitors_admin')) || 0;

        // KV에서 앱 클릭수 가져오기
        let appClicksData = await env.POFO_COUNTER.get('app_clicks');
        let appClicks = appClicksData ? JSON.parse(appClicksData) : {};

        let appClicksExtData = await env.POFO_COUNTER.get('app_clicks_external');
        let appClicksExternal = appClicksExtData ? JSON.parse(appClicksExtData) : {};

        let appClicksAdminData = await env.POFO_COUNTER.get('app_clicks_admin');
        let appClicksAdmin = appClicksAdminData ? JSON.parse(appClicksAdminData) : {};

        if (action === 'calibrate') {
            const extParam = url.searchParams.get('extCount');
            const adminParam = url.searchParams.get('adminCount');
            if (extParam !== null) totalVisitorsExternal = Math.max(0, parseInt(extParam) || 0);
            if (adminParam !== null) totalVisitorsAdmin = Math.max(0, parseInt(adminParam) || 0);
            totalVisitors = totalVisitorsExternal + totalVisitorsAdmin;

            await env.POFO_COUNTER.put('total_visitors', totalVisitors.toString());
            await env.POFO_COUNTER.put('total_visitors_external', totalVisitorsExternal.toString());
            await env.POFO_COUNTER.put('total_visitors_admin', totalVisitorsAdmin.toString());
        } else if (action === 'view') {
            totalVisitors += 1;
            if (isAdmin) {
                totalVisitorsAdmin += 1;
            } else {
                totalVisitorsExternal += 1;
            }
            await env.POFO_COUNTER.put('total_visitors', totalVisitors.toString());
            await env.POFO_COUNTER.put('total_visitors_external', totalVisitorsExternal.toString());
            await env.POFO_COUNTER.put('total_visitors_admin', totalVisitorsAdmin.toString());
        } else if (action === 'click' && appId) {
            appClicks[appId] = (appClicks[appId] || 0) + 1;
            if (isAdmin) {
                appClicksAdmin[appId] = (appClicksAdmin[appId] || 0) + 1;
            } else {
                appClicksExternal[appId] = (appClicksExternal[appId] || 0) + 1;
            }
            await env.POFO_COUNTER.put('app_clicks', JSON.stringify(appClicks));
            await env.POFO_COUNTER.put('app_clicks_external', JSON.stringify(appClicksExternal));
            await env.POFO_COUNTER.put('app_clicks_admin', JSON.stringify(appClicksAdmin));
        } else if (action === 'get') {
            // 조회만 수행
        } else {
            return new Response(JSON.stringify({ error: 'Invalid action' }), { status: 400, headers });
        }

        return new Response(JSON.stringify({
            total_visitors: totalVisitors,
            total_visitors_external: totalVisitorsExternal,
            total_visitors_admin: totalVisitorsAdmin,
            app_clicks: appClicks,
            app_clicks_external: appClicksExternal,
            app_clicks_admin: appClicksAdmin
        }), { status: 200, headers });

    } catch (error) {
        return new Response(JSON.stringify({ error: error.message }), { status: 500, headers });
    }
}
