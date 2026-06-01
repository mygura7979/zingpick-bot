import json
import os
from datetime import datetime

# 상품 데이터 (나중에 알리 API 연동으로 자동화)
products = [
    {"id": "001", "name": "Mini LED Flashlight 1000 Lumen", "price": 8.99, "emoji": "🔦", "category": "Tech Gadgets", "rating": 4.9, "reviews": 2341, "tag": "Hot Today", "desc": "Ultra-bright pocket flashlight with 1000 lumen output. Perfect for camping, emergencies, and everyday carry."},
    {"id": "002", "name": "Wireless Earbuds with Charging Case", "price": 14.99, "emoji": "🎧", "category": "Tech Gadgets", "rating": 4.4, "reviews": 1823, "tag": "Best Seller", "desc": "True wireless earbuds with deep bass, 4-hour playtime, and compact charging case. Works with all devices."},
    {"id": "003", "name": "Magnetic Phone Stand 360 Degree", "price": 6.49, "emoji": "📱", "category": "Tech Gadgets", "rating": 4.8, "reviews": 3102, "tag": "Trending", "desc": "Adjustable magnetic phone stand for desk. 360-degree rotation, foldable, compatible with all smartphones."},
    {"id": "004", "name": "Digital Kitchen Thermometer", "price": 9.99, "emoji": "🌡️", "category": "Home & Kitchen", "rating": 4.3, "reviews": 987, "tag": "New", "desc": "Instant-read digital thermometer for cooking. Accurate to 0.1°C, waterproof, foldable probe design."},
    {"id": "005", "name": "USB Mini Desk Fan", "price": 12.99, "emoji": "🌀", "category": "Home & Kitchen", "rating": 4.5, "reviews": 1456, "tag": "Best Seller", "desc": "Quiet USB-powered mini fan for desk use. 3 speed settings, 360-degree rotation, energy efficient."},
    {"id": "006", "name": "Cable Management Clips Pack 20", "price": 4.99, "emoji": "🔌", "category": "Tech Gadgets", "rating": 4.7, "reviews": 2789, "tag": "Hot Today", "desc": "Self-adhesive cable clips to organize your desk. Pack of 20, works on wood, glass, and plastic surfaces."},
    {"id": "007", "name": "Stainless Steel Water Bottle 500ml", "price": 11.99, "emoji": "🍶", "category": "Outdoor", "rating": 4.6, "reviews": 4231, "tag": "Trending", "desc": "Double-wall insulated water bottle. Keeps drinks cold 24hrs or hot 12hrs. Leak-proof, BPA-free."},
    {"id": "008", "name": "LED Strip Lights 2 Meter", "price": 7.99, "emoji": "💡", "category": "Home & Kitchen", "rating": 4.4, "reviews": 3567, "tag": "Hot Today", "desc": "USB-powered LED strip lights with remote control. 16 colors, dimmable, perfect for room decoration."},
    {"id": "009", "name": "Resistance Bands Set 5 Levels", "price": 13.99, "emoji": "💪", "category": "Health & Fitness", "rating": 4.8, "reviews": 2103, "tag": "Best Seller", "desc": "5-piece resistance band set for home workouts. Latex-free, suitable for all fitness levels, includes bag."},
    {"id": "010", "name": "Portable Phone Card Wallet", "price": 3.99, "emoji": "👛", "category": "Tech Gadgets", "rating": 4.5, "reviews": 5621, "tag": "Trending", "desc": "Slim stick-on card wallet for phone back. Holds 3 cards, RFID blocking, strong adhesive."},
    {"id": "011", "name": "Cat Laser Toy Interactive", "price": 5.99, "emoji": "🐱", "category": "Pet Supplies", "rating": 4.7, "reviews": 1892, "tag": "Hot Today", "desc": "Automatic rotating laser toy for cats. 3 speed modes, auto shut-off after 15 minutes, USB rechargeable."},
    {"id": "012", "name": "Foldable Laptop Stand Aluminum", "price": 18.99, "emoji": "💻", "category": "Tech Gadgets", "rating": 4.9, "reviews": 3241, "tag": "Best Seller", "desc": "Portable aluminum laptop stand with 6 height levels. Folds flat, supports up to 17-inch laptops."},
    {"id": "013", "name": "Silicone Kitchen Utensil Set 6 Pcs", "price": 15.99, "emoji": "🍳", "category": "Home & Kitchen", "rating": 4.6, "reviews": 1234, "tag": "New", "desc": "6-piece silicone kitchen tool set. Heat resistant up to 230°C, dishwasher safe, non-scratch."},
    {"id": "014", "name": "Bluetooth Key Finder Tracker", "price": 9.49, "emoji": "🔑", "category": "Tech Gadgets", "rating": 4.3, "reviews": 2876, "tag": "Trending", "desc": "Bluetooth key finder with app control. 30m range, loud alarm, works with iOS and Android."},
    {"id": "015", "name": "Microfiber Cleaning Cloth Set 10", "price": 6.99, "emoji": "🧹", "category": "Home & Kitchen", "rating": 4.8, "reviews": 6789, "tag": "Best Seller", "desc": "Pack of 10 premium microfiber cleaning cloths. Ultra-absorbent, lint-free, machine washable."},
    {"id": "016", "name": "Portable Jump Rope Speed", "price": 7.49, "emoji": "🎽", "category": "Health & Fitness", "rating": 4.6, "reviews": 1567, "tag": "Hot Today", "desc": "Speed jump rope with ball bearings for smooth rotation. Adjustable length, foam handles, great for cardio."},
    {"id": "017", "name": "Dog Chew Toy Rubber Durable", "price": 8.49, "emoji": "🐕", "category": "Pet Supplies", "rating": 4.7, "reviews": 2341, "tag": "Trending", "desc": "Durable rubber chew toy for dogs. Non-toxic, cleans teeth, suitable for medium to large dogs."},
    {"id": "018", "name": "Wireless Charging Pad 15W Fast", "price": 11.49, "emoji": "⚡", "category": "Tech Gadgets", "rating": 4.5, "reviews": 4123, "tag": "New", "desc": "15W fast wireless charging pad compatible with all Qi devices. LED indicator, overcharge protection."},
    {"id": "019", "name": "Bamboo Cutting Board Large", "price": 14.49, "emoji": "🔪", "category": "Home & Kitchen", "rating": 4.8, "reviews": 2987, "tag": "Best Seller", "desc": "Extra-large bamboo cutting board with juice groove. Eco-friendly, knife-friendly, easy to clean."},
    {"id": "020", "name": "Foam Roller Massage 33cm", "price": 16.99, "emoji": "🧘", "category": "Health & Fitness", "rating": 4.6, "reviews": 1876, "tag": "Hot Today", "desc": "High-density foam roller for muscle recovery. Grid pattern for deep tissue massage, lightweight."},
]

def generate_product_page(product):
    stars = "★" * int(product["rating"]) + "☆" * (5 - int(product["rating"]))
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
  .breadcrumb a{{color:var(--muted);text-decoration:none;}}
  .breadcrumb a:hover{{color:var(--accent);}}
  .product-wrap{{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:3rem;}}
  .product-img{{background:var(--surface);border:1px solid var(--border);border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:6rem;aspect-ratio:1;}}
  .product-info{{padding:0.5rem 0;}}
  .tag{{display:inline-block;background:rgba(245,197,24,0.1);border:1px solid rgba(245,197,24,0.3);color:var(--accent);font-size:0.72rem;font-weight:700;padding:0.25rem 0.8rem;border-radius:100px;margin-bottom:1rem;text-transform:uppercase;letter-spacing:0.06em;}}
  .product-info h1{{font-family:'Syne',sans-serif;font-size:1.8rem;font-weight:800;margin-bottom:0.8rem;line-height:1.2;letter-spacing:-0.02em;}}
  .rating{{display:flex;align-items:center;gap:0.5rem;margin-bottom:1.2rem;}}
  .stars{{color:var(--accent);font-size:0.9rem;}}
  .rating-num{{font-size:0.85rem;color:var(--muted);}}
  .price-wrap{{margin-bottom:1.5rem;}}
  .price{{font-family:'DM Sans',sans-serif;font-size:2.5rem;font-weight:700;color:var(--accent);letter-spacing:-0.02em;}}
  .price-sub{{font-size:0.85rem;color:var(--muted);margin-top:0.2rem;}}
  .cta-btn{{display:block;background:var(--accent);color:#0a0a0f;font-weight:700;font-size:1rem;padding:1rem 2rem;border-radius:10px;text-decoration:none;text-align:center;margin-bottom:1rem;transition:transform .2s,box-shadow .2s;}}
  .cta-btn:hover{{transform:translateY(-2px);box-shadow:0 8px 30px rgba(245,197,24,0.3);}}
  .desc-section{{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:1.5rem;margin-bottom:2rem;}}
  .desc-section h2{{font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:800;margin-bottom:0.8rem;}}
  .desc-section p{{color:#ccc;line-height:1.7;font-size:0.95rem;}}
  .notice{{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:1rem 1.4rem;font-size:0.8rem;color:var(--muted);margin:2rem 0;line-height:1.7;}}
  .notice strong{{color:var(--text);font-weight:600;}}
  footer{{border-top:1px solid var(--border);padding:2rem;text-align:center;color:var(--muted);font-size:0.82rem;}}
  footer a{{color:var(--muted);text-decoration:none;margin:0 0.8rem;}}
  @media(max-width:600px){{.product-wrap{{grid-template-columns:1fr;}}.product-info h1{{font-size:1.4rem;}}}}
</style>
</head>
<body>
<nav>
  <a href="/" class="logo">Zing<span>Pick</span></a>
  <a href="/" class="back">← Back to Picks</a>
</nav>
<div class="container">
  <div class="breadcrumb">
    <a href="/">Home</a> → <a href="/">{ product["category"]}</a> → {product["name"]}
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
      <a href="https://s.click.aliexpress.com/e/_c3pH1yq1" class="cta-btn" target="_blank" rel="nofollow">
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
    <a href="/">Home</a><a href="#">About</a><a href="#">Privacy Policy</a><a href="#">Affiliate Disclosure</a>
  </div>
  <div>© 2026 ZingPick.com — Best Gadgets Under $20</div>
</footer>
</body>
</html>"""

# 페이지 생성
os.makedirs("pages", exist_ok=True)
for p in products:
    filename = f"pages/product-{p['id']}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(generate_product_page(p))
    print(f"✅ 생성됨: {filename}")

print(f"\n총 {len(products)}개 상품 페이지 생성 완료!")
