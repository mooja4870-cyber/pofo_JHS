#!/usr/bin/env python3
"""보은 살아보기 신청서 이미지 모자이크 v5 - 누락 좌표 추가"""
from PIL import Image
import os

def mosaic(img, box, level=14):
    x1, y1, x2, y2 = box
    W, H = img.size
    x1, y1 = max(0,x1), max(0,y1)
    x2, y2 = min(W,x2), min(H,y2)
    if x2<=x1 or y2<=y1: return img
    region = img.crop((x1,y1,x2,y2))
    sm = region.resize((max(1,region.width//level), max(1,region.height//level)), Image.BOX)
    img.paste(sm.resize(region.size, Image.NEAREST), (x1,y1))
    return img

def process(fname, regions, base):
    orig = os.path.join(base, fname.replace('.jpg','_orig.jpg'))
    dst  = os.path.join(base, fname)
    img  = Image.open(orig).copy()
    for box in regions: img = mosaic(img, box)
    img.save(dst, quality=92)
    print(f"  저장: {fname}")

B = '/Users/l/project/pofo_JHS'

# ── 이미지1: 1999x2853 ──────────────────────────────────
# v4 적용 + 누락 항목 추가
i1 = [
    # 성 명 라벨 포함 + "정 호 식"
    (194, 462, 525, 506),
    # 연락처 라벨 + "010-2422-4511"
    (525, 462, 1445, 506),
    # 생년월일 라벨 + 날짜
    (194, 502, 585, 574),
    # 직업 라벨 + 크리에이터 (선택적, 공개가능 - 처리 안 함)
    # 주소 전체 (y:574~662 → 실제로는 더 아래)
    (194, 574, 1990, 680),
    # 팀참가자 성명 "김은미"
    (383, 1952, 665, 2000),
    # 팀참가자 나이 "59"
    (783, 1952, 930, 2000),
    # 팀참가자 성별행 + 연락처 "010-2912-1565" 전체
    (194, 2000, 1990, 2070),
    # 서명
    (905, 2445, 1820, 2582),
]

# ── 이미지2: 1975x2822 ──────────────────────────────────
i2 = [
    (194, 278, 1965, 358),   # 신청자 헤더 전체 행 (성명+연락처+생년월일)
    (820, 2460, 1762, 2618), # 서명
]

# ── 이미지3: 1984x2852 ──────────────────────────────────
i3 = [
    (832, 2488, 1762, 2658),
]

# ── 이미지4: 1880x2725 ──────────────────────────────────
i4 = [
    (802, 2328, 1770, 2510),
]

print("=== 모자이크 v5 ===")
for fname, regions in [
    ('boeun_apply_01.jpg', i1),
    ('boeun_apply_02.jpg', i2),
    ('boeun_apply_03.jpg', i3),
    ('boeun_apply_04.jpg', i4),
]:
    process(fname, regions, B)
print("=== 완료 ===")
