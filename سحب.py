from playwright.sync_api import sync_playwright
import time
import random

# ====================== الكوكيز (مدمجة) ======================
cookies = [
    {"name": "cookie_preferences_set_v2", "value": "%7B%22state%22%3A%7B%22preferences%22%3A%7B%22necessary%22%3Atrue%2C%22functional%22%3Atrue%2C%22performance%22%3Atrue%2C%22targeting%22%3Atrue%2C%22userHasMadeChoice%22%3Atrue%7D%2C%22functionalEnabled%22%3Atrue%2C%22performanceEnabled%22%3Atrue%2C%22targetingEnabled%22%3Atrue%7D%2C%22version%22%3A0%7D", "domain": ".kick.com", "path": "/", "secure": True},
    {"name": "kick_session_id", "value": "019dba8b-3f5e-7f3c-85a3-e3d6c3a28e79", "domain": "web.kick.com", "path": "/", "secure": True},
    {"name": "_ga", "value": "GA1.1.1569794332.1776951184", "domain": ".kick.com", "path": "/", "secure": False},
    {"name": "__stripe_mid", "value": "89e876aa-1d8b-48f5-b4c2-0bb3b7f69e770b5dc1", "domain": ".kick.com", "path": "/", "secure": True},
    {"name": "_gcl_au", "value": "1.1.893263949.1776951184.887393575.1776951192.1776951424", "domain": ".kick.com", "path": "/", "secure": False},
    {"name": "kick_session", "value": "eyJpdiI6ImxZMlVOcG5FUCs1azdQcTN0bGpIcnc9PSIsInZhbHVlIjoidldRSnBhdGJnTU5EcHlRdVFJRlBkeU1kcnRFaklKTlNhVHRIQzkwdGcxak1DdHNjYUJIWmdnemYzVCtabWRQVStLNGovWmJrWnJXQTA4M3Rzb0k5TUtxMUwxRkljSXlnTHd0ZnlFR25iSU5PNm8yTzhrejhVRnI3clliVU13TmkiLCJtYWMiOiJkY2UxZDJlNjNmZTJiN2E4NGNhNzMzZGJmNjExODc5YzU1ZWU3MzNlMGNkZmI3NDM2NmVhNGYwYzU3MGRjZTgzIiwidGFnIjoiIn0%3D", "domain": ".kick.com", "path": "/", "secure": False},
    {"name": "LKOfvytESsqulRhBrCMMBIKUNZoFPTYRpIr71ad3", "value": "eyJpdiI6IldiRUNmTDdub2FDV3dpdndUN2NqT2c9PSIsInZhbHVlIjoiOXczSVdjQVRRT2JQVkRzbXBTcUJib29jaU1WU2VlZ2pEaC9aTWtwR1VZOGtweS8rVTMwV3BaOXc2OU9vMzBrRVgwcEVTcG8rdHNPWld3QnZvWVBQRVd3UXp6NzZTaUorVytHZ3lSZ0t5bEJoa2g2QzB6STYvUHM5bmtXUFAwbGtYSmxWU0NpclRiL1BXUnROOHBOY2pnTEVkQW5vbGh1ZEREbUgzYnlJcE05NFp6MnBNM3kvbjNPbm1jU3hPck9lVHFQZ0VPT0l0KzkzRVFxb0JsbFB5NHJ3V00zd1JLZFF5QkRqK1FxQUVDRVJudW1uT3NNYjJBQ2RjV0RBdCtjK25pcnFZUm1rUGZpMnh0NDVzRmhtWnlYWXVwYmtDNURkRU9GU0JpMXdiMFYrRXdBUldwY0ZZbE1QR0F1MVM2NDlxSmUrWnhacGg4SFJDd0k1VE9xSy85QTdJR2lFT3Z3b2lWcmNvYnZoNDVLeEJOSzA5bWpqMm1MQkZabm1iTWt0IiwibWFjIjoiZDJiNDExOWMyMTc2M2ZmZGI3NmRjNzE4ODQ1NTRmZDBkOGExMTQ3NTBhYTYxYTg0MDEyNTg0NDFiODRkNDEwZSIsInRhZyI6IiJ9", "domain": ".kick.com", "path": "/", "secure": False},
    {"name": "XSRF-TOKEN", "value": "eyJpdiI6IkhDcnZiWEFLZEF1dUw5WUhHemtHbkE9PSIsInZhbHVlIjoiYTFHMGdrVHZ5ZlpHYnp0c05aRFdnRU1qSjVPb3IyK05TQlM1ZFdyTlovNnB6Mm1CVEdpWkt6bUlzYVBMSU9scmgyMFdKKy9WTVg2N05FRW4zdWl0SGlHbmcxNjZ4U0RGMk01S2tJZnY4bzlDOHd1K1dsUVpZdlNuVGIvNCtsN28iLCJtYWMiOiJmZmEzZDE4NmQ4YmZkZWQ5Y2M1MGZmNTQ5MzM0ZWQyZTM4YWE4NzhjMjhjZmFiMmE0ZmJiZWZiY2U3MTIyYmYyIiwidGFnIjoiIn0%3D", "domain": ".kick.com", "path": "/", "secure": False},
    {"name": "session_token", "value": "354125256%7Cl1cSwekqy1f6V5d8bccoY5KLBrL3HhA367Gp2vjm", "domain": ".kick.com", "path": "/", "secure": True},
    {"name": "_ga_S2K66B788M", "value": "GS2.1.s1777583426$o2$g0$t1777583459$j27$l0$h0", "domain": ".kick.com", "path": "/", "secure": False},
    {"name": "volume", "value": "0.21", "domain": "kick.com", "path": "/", "secure": False},
    {"name": "__cf_bm", "value": "DVvmp5Gi.zA6JCl2guuNLIh3V4vegOCFimSIM1wejpo-1778267219.561612-1.0.1.1-JOjz6WtR7HNZM_BfQx6j76dB7L3lQ._qvHjuMOPI6aRT10zjIfKY.rdRRkdk3HDoNcb_XZznXTC8tdTTaK4nj7Sn.1mtC.F8CD.CsQK_fRJ4LblLM5XEM41OPFPfx1qo", "domain": ".kick.com", "path": "/", "secure": True},
]

# ====================== الإعدادات ======================
channel_url = "https://kick.com/7anteraagaming"   # ← غير الاسم ده بالستريمر اللي عايزه

messages = [
    "يا سلام على الستريم",
    "keep going bro",
    "nice stream 🔥",
    "الله يبارك فيك",
    "🔥🔥🔥",
    "very good",
    "كمل يا وحش",
    "insane 🔥",
    "ماشي تمام",
    "love the stream",
    "هههههه",
    "based",
    "let's gooo",
    "good job",
    "❤️"
]

# ====================== تشغيل البوت ======================
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    
    context = browser.new_context(
        viewport={'width': 1280, 'height': 900},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    )
    
    context.add_cookies(cookies)
    print("✅ تم تحميل الكوكيز بنجاح")
    
    page = context.new_page()
    
    while True:
        try:
            print(f"جاري الدخول إلى: {channel_url}")
            page.goto(channel_url, wait_until="networkidle", timeout=60000)
            
            print("🚀 البوت شغال دلوقتي... (Ctrl + C عشان توقفه)")
            
            while True:
                try:
                    # selectors متعددة عشان تكون أقوى
                    chat_input = page.locator('input[placeholder*="Message" i], textarea[placeholder*="Message" i], [role="textbox"], div[contenteditable="true"]').first
                    
                    if chat_input.is_visible(timeout=5000):
                        msg = random.choice(messages)
                        chat_input.fill(msg)
                        chat_input.press("Enter")
                        print(f"✅ تم إرسال: {msg}")
                    else:
                        print("⚠️ مش لاقي خانة الكتابة")
                        
                except Exception as e:
                    print(f"خطأ في الإرسال: {e}")
                
                # تأخير بين 55 و 75 ثانية
                time.sleep(55 + random.uniform(0, 20))
                
        except Exception as e:
            print(f"خطأ كبير: {e} → هعيد المحاولة بعد 15 ثانية")
            time.sleep(15)