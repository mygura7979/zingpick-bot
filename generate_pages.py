import json
import os
from urllib.parse import quote

# 어필리에이트 트래킹 ID
AFFILIATE_ID = "c3pH1yq1"

def make_ali_link(search_keyword):
    """상품명으로 알리 검색결과 + 어필리에이트 링크 생성"""
    encoded = quote(search_keyword)
    return f"https://www.aliexpress.com/wholesale?SearchText={encoded}&aff_fcid={AFFILIATE_ID}&aff_platform=portals-tool"

# 상품 데이터
products = [
    {"id": "001", "name": "Mini LED Flashlight 1000 Lumen", "price": 8.99, "emoji": "🔦", "category": "Tech Gadgets", "rating": 4.9, "reviews": 2341, "tag": "Hot Today", "search": "mini LED flashlight 1000 lumen", "desc": "Ultra-bright pocket flashlight with 1000 lumen output. Perfect for camping, emergencies, and everyday carry."},
    {"id": "002", "name": "Wireless Earbuds with Charging Case", "price": 14.99, "emoji": "🎧", "category": "Tech Gadgets", "rating": 4.4, "reviews": 1823, "tag": "Best Seller", "search": "wireless earbuds charging case", "desc": "True wireless earbuds with deep bass, 4-hour playtime, and compact charging case. Works with all devices."},
    {"id": "003", "name": "Magnetic Phone Stand 360 Degree", "price": 6.49, "emoji": "📱", "category": "Tech Gadgets", "rating": 4.8, "reviews": 3102, "tag": "Trending", "search": "magnetic phone stand 360 degree", "desc": "Adjustable magnetic phone stand for desk. 360-degree rotation, foldable, compatible with all smartphones."},
    {"id": "004", "name": "Digital Kitchen Thermometer", "price": 9.99, "emoji": "🌡️", "category": "Home & Kitchen", "rating": 4.3, "reviews": 987, "tag": "New", "search": "digital kitchen thermometer instant read", "desc": "Instant-read digital thermometer for cooking. Accurate to 0.1°C, waterproof, foldable probe design."},
    {"id": "005", "name": "USB Mini Desk Fan", "price": 12.99, "emoji": "🌀", "category": "Home & Kitchen", "rating": 4.5, "reviews": 1456, "tag": "Best Seller", "search": "USB mini desk fan quiet", "desc": "Quiet USB-powered mini fan for desk use. 3 speed settings, 360-degree rotation, energy efficient."},
    {"id": "006", "name": "Cable Management Clips Pack 20", "price": 4.99, "emoji": "🔌", "category": "Tech Gadgets", "rating": 4.7, "reviews": 2789, "tag": "Hot Today", "search": "cable management clips adhesive", "desc": "Self-adhesive cable clips to organize your desk. Pack of 20, works on wood, glass, and plastic surfaces."},
    {"id": "007", "name": "Stainless Steel Water Bottle 500ml", "price": 11.99, "emoji": "🍶", "category": "Outdoor", "rating": 4.6, "reviews": 4231, "tag": "Trending", "search": "stainless steel water bottle insulated 500ml", "desc": "Double-wall insulated water bottle. Keeps drinks cold 24hrs or hot 12hrs. Leak-proof, BPA-free."},
    {"id": "008", "name": "LED Strip Lights 2 Meter", "price": 7.99, "emoji": "💡", "category": "Home & Kitchen", "rating": 4.4, "reviews": 3567, "tag": "Hot Today", "search": "LED strip lights RGB 2 meter USB", "desc": "USB-powered LED strip lights with remote control. 16 colors, dimmable, perfect for room decoration."},
    {"id": "009", "name": "Resistance Bands Set 5 Levels", "price": 13.99, "emoji": "💪", "category": "Health & Fitness", "rating": 4.8, "reviews": 2103, "tag": "Best Seller", "search": "resistance bands set 5 levels workout", "desc": "5-piece resistance band set for home workouts. Latex-free, suitable for all fitness levels, includes bag."},
    {"id": "010", "name": "Portable Phone Card Wallet", "price": 3.99, "emoji": "👛", "category": "Tech Gadgets", "rating": 4.5, "reviews": 5621, "tag": "Trending", "search": "phone card wallet RFID stick on", "desc": "Slim stick-on card wallet for phone back. Holds 3 cards, RFID blocking, strong adhesive."},
    {"id": "011", "name": "Cat Laser Toy Interactive", "price": 5.99, "emoji": "🐱", "category": "Pet Supplies", "rating": 4.7, "reviews": 1892, "tag": "Hot Today", "search": "cat laser toy automatic interactive", "desc": "Automatic rotating laser toy for cats. 3 speed modes, auto shut-off after 15 minutes, USB rechargeable."},
    {"id": "012", "name": "Foldable Laptop Stand Aluminum", "price": 18.99, "emoji": "💻", "category": "Tech Gadgets", "rating": 4.9, "reviews": 3241, "tag": "Best Seller", "search": "foldable laptop stand aluminum portable", "desc": "Portable aluminum laptop stand with 6 height levels. Folds flat, supports up to 17-inch laptops."},
    {"id": "013", "name": "Silicone Kitchen Utensil Set 6 Pcs", "price": 15.99, "emoji": "🍳", "category": "Home & Kitchen", "rating": 4.6, "reviews": 1234, "tag": "New", "search": "silicone kitchen utensil set 6 piece", "desc": "6-piece silicone kitchen tool set. Heat resistant up to 230°C, dishwasher safe, non-scratch."},
    {"id": "014", "name": "Bluetooth Key Finder Tracker", "price": 9.49, "emoji": "🔑", "category": "Tech Gadgets", "rating": 4.3, "reviews": 2876, "tag": "Trending", "search": "bluetooth key finder tracker smart", "desc": "Bluetooth key finder with app control. 30m range, loud alarm, works with iOS and Android."},
    {"id": "015", "name": "Microfiber Cleaning Cloth Set 10", "price": 6.99, "emoji": "🧹", "category": "Home & Kitchen", "rating": 4.8, "reviews": 6789, "tag": "Best Seller", "search": "microfiber cleaning cloth set 10 pack", "desc": "Pack of 10 premium microfiber cleaning cloths. Ultra-absorbent, lint-free, machine washable."},
    {"id": "016", "name": "Portable Jump Rope Speed", "price": 7.49, "emoji": "🎽", "category": "Health & Fitness", "rating": 4.6, "reviews": 1567, "tag": "Hot Today", "search": "speed jump rope bearing handles", "desc": "Speed jump rope with ball bearings for smooth rotation. Adjustable length, foam handles, great for cardio."},
    {"id": "017", "name": "Dog Chew Toy Rubber Durable", "price": 8.49, "emoji": "🐕", "category": "Pet Supplies", "rating": 4.7, "reviews": 2341, "tag": "Trending", "search": "dog chew toy rubber durable non-toxic", "desc": "Durable rubber chew toy for dogs. Non-toxic, cleans teeth, suitable for medium to large dogs."},
    {"id": "018", "name": "Wireless Charging Pad 15W Fast", "price": 11.49, "emoji": "⚡", "category": "Tech Gadgets", "rating": 4.5, "reviews": 4123, "tag": "New", "search": "wireless charging pad 15W fast Qi", "desc": "15W fast wireless charging pad compatible with all Qi devices. LED indicator, overcharge protection."},
    {"id": "019", "name": "Bamboo Cutting Board Large", "price": 14.49, "emoji": "🔪", "category": "Home & Kitchen", "rating": 4.8, "reviews": 2987, "tag": "Best Seller", "search": "bamboo cutting board large kitchen", "desc": "Extra-large bamboo cutting board with juice groove. Eco-friendly, knife-friendly, easy to clean."},
    {"id": "020", "name": "Foam Roller Massage 33cm", "price": 16.99, "emoji": "🧘", "category": "Health & Fitness", "rating": 4.6, "reviews": 1876, "tag": "Hot Today", "search": "foam roller massage muscle recovery", "desc": "High-density foam roller for muscle recovery. Grid pattern for deep tissue massage, lightweight."},
]

def generate_product_page(product):
    stars = "★" * int(product["rating"]) + "☆" * (5 - int(product["rating"]))
    ali_link = make_ali_link(product["search"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{product["name"]} — Under $20 | ZingPick</title>
<meta name="description" content="Get {product["name"]} for only ${product["price"]}. {product["desc"]} Shop the best deals under $20 at ZingPick.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{{--bg:#0a0a0f;--surface:#13131a;--border:#1e1e2e;--accent:#f5c518;--accent2:#ff6b35;--text:#f0f0f0;--muted:#888;}}
  *{{margin:0;padding:0;box-sizing:border-box;}}
  body{{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;min-height:100vh;}}
  nav{{display:flex;align-items:center;justify-content:space-between;padding:1.2rem 2rem;border-bottom:1px solid var(--border);background:rgba(10,10,15,0.92);backdrop-filter:blur(12px);position:sticky;top:0;z-index:100;}}
  .logo{{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;color:var(--accent);text-decoration:none;}}
  .logo span{{color:var(--accent2);}}
  .back{{color:var(--muted);text-decoration:none;font-size:0.9rem;}}
  .back:hover{{color:var(--text);}}
  .container{{max-width:900px;margin:0 auto;padding:3rem 2rem;}}
  .breadcrumb{{font-size:0.8rem;color:var(--muted);margin-bottom:2rem;}}
  .product-wrap{{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:3rem;}}
  .product-img{{background:var(--surface);border:1px solid var(--border);border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:6rem;aspect-ratio:1;}}
  .product-info{{padding:0.5rem 0;}}
  .tag{{display:inline-block;background:rgba(245,197,24,0.1);border:1px solid rgba(245,197,24,0.3);color:var(--accent);font-size:0.72rem;font-weight:700;padding:0.25rem 0.8rem;border-radius:100px;margin-bottom:1rem;text-transform:uppercase;letter-spacing:0.06em;}}
  .product-info h1{{font-family:'Syne',sans-serif;font-size:1.8rem;font-weight:800;margin-bottom:0.8rem;line-height:1.2;}}
  .rating{{display:flex;align-items:center;gap:0.5rem;margin-bottom:1.2rem;}}
  .stars{{color:var(--accent);font-size:0.9rem;}}
  .rating-num{{font-size:0.85rem;color:var(--muted);}}
  .price-wrap{{margin-bottom:1.5rem;}}
  .price{{font-size:2.5rem;font-weight:700;color:var(--accent);}}
  .price-sub{{font-size:0.85rem;color:var(--muted);margin-top:0.2rem;}}
  .cta-btn{{display:block;background:var(--accent);color:#0a0a0f;font-weight:700;font-size:1rem;padding:1rem 2rem;border-radius:10px;text-decoration:none;text-align:center;margin-bottom:1rem;transition:transform .2s,box-shadow .2s;}}
  .cta-btn:hover{{transform:translateY(-2px);box-shadow:0 8px 30px rgba(245,197,24,0.3);}}
  .desc-section{{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:1.5rem;margin-bottom:2rem;}}
  .desc-section h2{{font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:800;margin-bottom:0.8rem;}}
  .desc-section p{{color:#ccc;line-height:1.7;font-size:0.95rem;}}
  .notice{{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:1rem 1.4rem;font-size:0.8rem;color:var(--muted);margin:2rem 0;line-height:1.7;}}
  footer{{border-top:1px solid var(--border);padding:2rem;text-align:center;color:var(--muted);font-size:0.82rem;}}
  footer a{{color:var(--muted);text-decoration:none;margin:0 0.8rem;}}
  @media(max-width:600px){{.product-wrap{{grid-template-columns:1fr;}}}}
</style>
</head>
<body>
<nav>
  <a href="/" class="logo">Zing<span>Pick</span></a>
  <a href="/" class="back">← Back to Picks</a>
</nav>
<div class="container">
  <div class="breadcrumb">
    <a href="/">Home</a> → {product["category"]} → {product["name"]}
  </div>
  <div class="product-wrap">
    <div class="product-img">{product["emoji"]}</div>
    <div class="product-info">
      <div class="tag">{product["tag"]}</div>
      <h1>{product["name"]}</h1>
      <div class="rating">
        <span class="stars">{stars}</span>
        <span class="rating-num">{product["rating"]} ({product["reviews"]:,} reviews)</span>
      </div>
      <div class="price-wrap">
        <div class="price">${product["price"]}</div>
        <div class="price-sub">Free shipping • In stock</div>
      </div>
      <a href="{ali_link}" class="cta-btn" target="_blank" rel="nofollow noopener">
        View Deal on AliExpress →
      </a>
    </div>
  </div>
  <div class="desc-section">
    <h2>Product Description</h2>
    <p>{product["desc"]}</p>
  </div>
  <div class="notice">
    <strong>Affiliate Disclosure:</strong> ZingPick participates in the AliExpress affiliate program. When you click our links and make a purchase, we may earn a small commission at no extra cost to you.
  </div>
</div>
<footer>
  <div style="margin-bottom:1rem;">
    <a href="/">Home</a><a href="#">Privacy Policy</a><a href="#">Affiliate Disclosure</a>
  </div>
  <div>© 2026 ZingPick.com — Best Gadgets Under $20</div>
</footer>
</body>
</html>"""

def generate_index():
    cards = ""
    for p in products:
        stars_full = int(p["rating"])
        stars_html = "★" * stars_full + "☆" * (5 - stars_full)
        cards += f"""
    <div class="card">
      <div class="card-img">{p["emoji"]}</div>
      <div class="card-body">
        <div class="card-tag">{p["tag"]}</div>
        <div class="card-stars">{stars_html} {p["rating"]}</div>
        <div class="card-name">{p["name"]}</div>
        <div class="card-bottom">
          <span class="card-price">${p["price"]}</span>
          <a href="/product-{p['id']}.html" class="deal-btn">View Deal</a>
        </div>
      </div>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ZingPick — Best Gadgets Under $20</title>
<meta name="description" content="Handpicked cool gadgets under $20. Updated daily. Weird, useful, and surprisingly cheap finds from AliExpress.">
<meta name="google-site-verification" content="FzoRvl9cHrVod1lj3iaOrRupP6QbcFn7yaKU2Z_qATY" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root{{--bg:#0a0a0f;--surface:#13131a;--border:#1e1e2e;--accent:#f5c518;--accent2:#ff6b35;--text:#f0f0f0;--muted:#888;}}
  *{{margin:0;padding:0;box-sizing:border-box;}}
  body{{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;}}
  nav{{display:flex;align-items:center;justify-content:space-between;padding:1.2rem 2rem;border-bottom:1px solid var(--border);background:rgba(10,10,15,0.95);position:sticky;top:0;z-index:100;}}
  .logo{{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;color:var(--accent);text-decoration:none;}}
  .logo span{{color:var(--accent2);}}
  .hero{{text-align:center;padding:5rem 2rem 3rem;}}
  .hero h1{{font-family:'Syne',sans-serif;font-size:3.5rem;font-weight:800;line-height:1.1;margin-bottom:1rem;}}
  .hero h1 span{{color:var(--accent);}}
  .hero p{{color:var(--muted);font-size:1.1rem;max-width:500px;margin:0 auto 2rem;}}
  .grid{{max-width:1200px;margin:0 auto;padding:2rem;display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1.5rem;}}
  .card{{background:var(--surface);border:1px solid var(--border);border-radius:16px;overflow:hidden;transition:transform .2s,border-color .2s;}}
  .card:hover{{transform:translateY(-4px);border-color:var(--accent);}}
  .card-img{{background:#1a1a24;display:flex;align-items:center;justify-content:center;font-size:4rem;padding:2rem;}}
  .card-body{{padding:1.2rem;}}
  .card-tag{{display:inline-block;background:rgba(245,197,24,0.1);border:1px solid rgba(245,197,24,0.3);color:var(--accent);font-size:0.68rem;font-weight:700;padding:0.2rem 0.6rem;border-radius:100px;margin-bottom:0.5rem;text-transform:uppercase;}}
  .card-stars{{color:var(--accent);font-size:0.75rem;margin-bottom:0.4rem;}}
  .card-name{{font-weight:600;font-size:0.95rem;margin-bottom:1rem;line-height:1.4;}}
  .card-bottom{{display:flex;align-items:center;justify-content:space-between;}}
  .card-price{{font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:var(--accent);}}
  .deal-btn{{background:var(--accent);color:#0a0a0f;font-weight:700;font-size:0.82rem;padding:0.5rem 1rem;border-radius:8px;text-decoration:none;transition:background .2s;}}
  .deal-btn:hover{{background:#e6b800;}}
  footer{{border-top:1px solid var(--border);padding:2rem;text-align:center;color:var(--muted);font-size:0.82rem;margin-top:3rem;}}
  footer a{{color:var(--muted);text-decoration:none;margin:0 0.8rem;}}
  @media(max-width:600px){{.hero h1{{font-size:2.2rem;}}}}
</style>
</head>
<body>
<nav>
  <a href="/" class="logo">Zing<span>Pick</span></a>
</nav>
<div class="hero">
  <h1>Cool Gadgets<br><span>Under $20</span></h1>
  <p>Handpicked finds from around the world. Weird, useful, and surprisingly cheap. Updated daily.</p>
</div>
<div class="grid">
  {cards}
</div>
<footer>
  <div style="margin-bottom:0.5rem;">
    <a href="#">Privacy Policy</a><a href="#">Affiliate Disclosure</a>
  </div>
  <div>© 2026 ZingPick.com — Best Gadgets Under $20</div>
  <div style="margin-top:0.5rem;font-size:0.75rem;">We earn a commission from AliExpress when you purchase through our links.</div>
</footer>
</body>
</html>"""

# 페이지 생성
os.makedirs("pages", exist_ok=True)

with open("pages/index.html", "w", encoding="utf-8") as f:
    f.write(generate_index())
print("✅ 생성됨: pages/index.html")

for p in products:
    filename = f"pages/product-{p['id']}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(generate_product_page(p))
    print(f"✅ 생성됨: {filename}")

print(f"\n총 {len(products)+1}개 파일 생성 완료!")

# sitemap.xml 자동 생성
sitemap_urls = ['<url><loc>https://zingpick.com/</loc><changefreq>daily</changefreq><priority>1.0</priority></url>']
for p in products:
    sitemap_urls.append(f'<url><loc>https://zingpick.com/product-{p["id"]}.html</loc><changefreq>daily</changefreq><priority>0.8</priority></url>')

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += '\n'.join(sitemap_urls)
sitemap += '\n</urlset>'

with open("pages/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)
print("✅ 생성됨: pages/sitemap.xml")

# _headers 파일 생성 (Cloudflare 스크립트 주입 방지)
headers = """/sitemap.xml
  Content-Type: application/xml
  X-Robots-Tag: noindex

/*.html
  X-Frame-Options: DENY
"""
with open("pages/_headers", "w", encoding="utf-8") as f:
    f.write(headers)
print("✅ 생성됨: pages/_headers")
