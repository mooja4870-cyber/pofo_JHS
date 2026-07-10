export async function onRequest(context) {
    const { request, env } = context;
    const url = new URL(request.url);
    const action = url.searchParams.get('action');
    const appId = url.searchParams.get('appId');

    const headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    };

    try {
        // KV에서 현재 값 가져오기
        let totalVisitors = parseInt(await env.POFO_COUNTER.get('total_visitors')) || 0;
        
        let appClicksData = await env.POFO_COUNTER.get('app_clicks');
        let appClicks = appClicksData ? JSON.parse(appClicksData) : {};

        if (action === 'view') {
            // 조회수 1 증가
            totalVisitors += 1;
            await env.POFO_COUNTER.put('total_visitors', totalVisitors.toString());
        } else if (action === 'click' && appId) {
            // 특정 앱 클릭수 1 증가
            if (!appClicks[appId]) {
                appClicks[appId] = 0;
            }
            appClicks[appId] += 1;
            await env.POFO_COUNTER.put('app_clicks', JSON.stringify(appClicks));
        } else {
            return new Response(JSON.stringify({ error: 'Invalid action' }), { status: 400, headers });
        }

        // 업데이트된 최신 데이터 반환
        return new Response(JSON.stringify({
            total_visitors: totalVisitors,
            app_clicks: appClicks
        }), { status: 200, headers });

    } catch (error) {
        return new Response(JSON.stringify({ error: error.message }), { status: 500, headers });
    }
}
