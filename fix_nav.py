import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Define active classes
    def get_class(link):
        return 'text-amber-400' if f == link else 'hover:text-amber-400'

    nav_html = f"""<!-- NAVIGATION -->
    <nav class="bg-zinc-950 border-b border-zinc-800 fixed w-full z-50">
        <div class="max-w-7xl mx-auto px-6">
            <div class="flex justify-between items-center h-20">
                <div class="flex items-center gap-3">
                    <img src="logo.jpeg" alt="Logo" class="h-12 w-auto">
                    <div>
                        <span class="text-2xl font-bold tracking-tighter">SAMMY SHARP</span>
                        <span class="block text-xs text-amber-400 -mt-1">OIL & GAS LIMITED</span>
                    </div>
                </div>
                <div class="hidden md:flex items-center gap-8 text-sm font-medium">
                    <a href="index.html" class="{get_class('index.html')}">HOME</a>
                    <a href="about.html" class="{get_class('about.html')}">ABOUT US</a>
                    <a href="operations.html" class="{get_class('operations.html')}">OPERATIONS</a>
                    <a href="gallery.html" class="{get_class('gallery.html')}">GALLERY</a>
                    <a href="locate.html" class="{get_class('locate.html')}">LOCATE US</a>
                    <a href="contact.html" class="{get_class('contact.html')}">CONTACT</a>
                    <a href="teams.html" class="{get_class('teams.html')}">TEAM</a>
                </div>
                <button onclick="toggleMobileMenu()" class="md:hidden text-3xl"><i class="fa-solid fa-bars"></i></button>
            </div>
        </div>
        <div id="mobileMenu" class="hidden md:hidden bg-zinc-900 border-t border-zinc-800 py-6">
            <div class="flex flex-col gap-6 px-6 text-lg">
                <a href="index.html" class="{get_class('index.html')}">HOME</a>
                <a href="about.html" class="{get_class('about.html')}">ABOUT US</a>
                <a href="operations.html" class="{get_class('operations.html')}">OPERATIONS</a>
                <a href="gallery.html" class="{get_class('gallery.html')}">GALLERY</a>
                <a href="locate.html" class="{get_class('locate.html')}">LOCATE US</a>
                <a href="contact.html" class="{get_class('contact.html')}">CONTACT</a>
                <a href="teams.html" class="{get_class('teams.html')}">TEAM</a>
            </div>
        </div>
    </nav>"""

    new_content = re.sub(r'<!-- NAVIGATION -->.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

print("Fixed navigation in all HTML files.")
