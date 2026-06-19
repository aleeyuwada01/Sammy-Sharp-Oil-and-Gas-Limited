import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Hero title
    content = content.replace('class="text-6xl md:text-7xl', 'class="text-4xl md:text-6xl lg:text-7xl')
    
    # Normal h1 titles
    content = content.replace('class="text-6xl font-bold"', 'class="text-4xl md:text-6xl font-bold"')
    content = content.replace('class="text-6xl font-bold mb-6"', 'class="text-4xl md:text-6xl font-bold mb-6"')
    
    # h2 titles
    content = content.replace('class="text-5xl font-bold"', 'class="text-3xl md:text-5xl font-bold"')
    content = content.replace('class="text-5xl font-bold text-white mb-2"', 'class="text-3xl md:text-5xl font-bold text-white mb-2"')
    content = content.replace('class="text-5xl font-bold mb-8"', 'class="text-3xl md:text-5xl font-bold mb-8"')
    
    # Button group in hero
    content = content.replace('class="flex gap-4"', 'class="flex flex-col sm:flex-row gap-4"')
    
    # Update logo in nav block to scale down slightly on mobile to avoid touching hamburger
    content = content.replace('class="text-2xl font-bold tracking-tighter"', 'class="text-xl md:text-2xl font-bold tracking-tighter"')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Responsive classes updated in all HTML files.")
