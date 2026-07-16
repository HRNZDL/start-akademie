import re

with open('assets/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix 1: iOS backdrop-filter on .glass-card
css = css.replace(
'''        .glass-card {
            background: rgba(18, 18, 22, 0.45);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 48px;
            backdrop-filter: blur(24px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
            transition: var(--transition);
        }''',
'''        .glass-card {
            background: rgba(14, 16, 21, 0.5); /* Improved fallback background for mobile */
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 48px;
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
            transition: var(--transition);
        }'''
)

# Fix 2: startbot-window and chat-msg UI
old_startbot = '''        .startbot-window {
            position: fixed;
            bottom: 80px;
            right: 0;
            width: 360px;
            height: 480px;
            /* Premium Dark Mode Glass */
            background: rgba(18, 18, 22, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;'''

new_startbot = '''        .startbot-window {
            position: fixed; /* Changed to fixed so it stays in viewport while scrolling */
            bottom: 80px;
            right: 20px;
            width: 350px;
            height: 460px;
            /* Premium Dark Mode Glass */
            background: rgba(14, 16, 21, 0.85);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 28px;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.7), 0 0 40px rgba(212, 175, 100, 0.08), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;'''

css = css.replace(old_startbot, new_startbot)

old_startbot_light = '''        :root[data-theme="light"] .startbot-window {
            background: rgba(255, 255, 255, 0.75);
            border: 1px solid rgba(0, 0, 0, 0.1);
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.15), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
        }'''

new_startbot_light = '''        :root[data-theme="light"] .startbot-window {
            background: rgba(255, 255, 255, 0.85);
            border: 1px solid rgba(0, 0, 0, 0.08);
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.12), 0 0 40px rgba(212, 175, 100, 0.1), 0 0 0 1px rgba(255, 255, 255, 0.6) inset;
        }'''

css = css.replace(old_startbot_light, new_startbot_light)

old_chat_msg = '''        .chat-msg {
            padding: 10px 14px;
            border-radius: 8px;
            font-size: 0.88rem;
            max-width: 80%;
            line-height: 1.5;
        }

        .chat-msg.bot {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #ffffff !important;
            align-self: flex-start;
        }
        .startbot-window {
            z-index: 999999;
        }
        .chat-msg.bot strong {
            color: var(--gold-light);
        }
        

        .chat-msg.user {
            background: var(--gold);
            color: var(--bg-deep);
            align-self: flex-end;
            font-weight: 500;
        }'''

new_chat_msg = '''        .chat-msg {
            padding: 12px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            max-width: 85%;
            line-height: 1.5;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .chat-msg.bot {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: #ffffff !important;
            align-self: flex-start;
            border-bottom-left-radius: 6px;
        }
        .startbot-window {
            z-index: 999999;
        }
        .chat-msg.bot strong {
            color: var(--gold-light);
        }
        

        .chat-msg.user {
            background: linear-gradient(135deg, var(--gold), var(--gold-light));
            color: var(--bg-deep);
            align-self: flex-end;
            font-weight: 500;
            border-bottom-right-radius: 6px;
            border: none;
        }'''

css = css.replace(old_chat_msg, new_chat_msg)

old_mobile_startbot = '''    /* StartBot Chat Window */
    .startbot-window { 
        width: 100% !important; 
        right: 0 !important; 
        bottom: 0 !important; 
        height: 85vh !important; 
        border-radius: 24px 24px 0 0 !important; 
    }'''

new_mobile_startbot = '''    /* StartBot Chat Window */
    .startbot-window { 
        width: calc(100% - 32px) !important; 
        right: 16px !important; 
        bottom: 80px !important; 
        height: 60vh !important; 
        max-height: 460px !important;
        border-radius: 20px !important; 
    }'''

css = css.replace(old_mobile_startbot, new_mobile_startbot)

with open('assets/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated safely!")
