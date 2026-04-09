import os

files = ['index.html', 'tentang.html', 'produk.html', 'kontak.html']

header_logo_replacement = '''<div class="logo">
            <a href="index.html" style="display:flex; align-items:center;">
                <img src="images/logo.png" alt="Logo Tirami" class="brand-logo">
            </a>
        </div>'''

footer_logo_replacement = '''<div class="footer-logo">
                <img src="images/logo.png" alt="Logo Tirami" class="brand-logo-footer">
            </div>'''

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # For index.html
    content = content.replace('''<div class="logo">
            <div class="logo-icon"><i class="fas fa-tree"></i></div> <!-- Placeholder for mushroom icon -->
            <div class="logo-text">
                <h2><span class="ti">Ti</span><span class="rami">rami</span></h2>
                <p>Enaknya Nugget, Sehatnya Jamur</p>
            </div>
        </div>''', header_logo_replacement)

    # For other htmls
    content = content.replace('''<div class="logo">
            <div class="logo-icon"><i class="fas fa-tree" style="color: var(--secondary);"></i></div>
            <div class="logo-text">
                <h2><span class="ti">Ti</span><span class="rami">rami</span></h2>
                <p style="font-size: 0.65rem; color: var(--primary); font-weight: 600; margin: 0;">Enaknya Nugget, Sehatnya Jamur</p>
            </div>
        </div>''', header_logo_replacement)
        
    # Footer index.html
    content = content.replace('''<div class="footer-logo">
                <span class="ti">Ti</span><span class="rami">rami</span>
            </div>''', footer_logo_replacement)
            
    # Footer others
    content = content.replace('''<div class="footer-logo">
                <span class="ti" style="color: var(--primary); font-weight: 800; font-size: 1.5rem;">Ti</span><span class="rami" style="color: var(--secondary); font-weight: 800; font-size: 1.5rem;">rami</span>
            </div>''', footer_logo_replacement)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write('\n\n/* Brand Logo Styles */\n.brand-logo { height: 65px; width: auto; object-fit: contain; }\n.brand-logo-footer { height: 50px; width: auto; opacity: 0.9; }')
