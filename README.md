# Amber Modern - Self-Hostable Static Site

This is a converted Squarespace website export that has been made self-hostable without requiring Squarespace's backend services.

## What's Been Converted

✅ **Static Content**: All HTML, CSS, images, and JavaScript files are included and work offline  
✅ **URL Remapping**: The `rerouter.js` file handles remapping Squarespace CDN URLs to local files  
✅ **External Dependencies Removed**: Removed external Squarespace CDN links for components  
✅ **Typekit Fonts**: Font loading from Adobe Typekit is preserved (requires internet connection)

## What Doesn't Work

❌ **Forms**: Contact forms and other form submissions require a backend replacement  
❌ **Shopping Cart**: E-commerce functionality requires a backend (cart page exists but won't process orders)  
❌ **Search**: Search functionality may not work without Squarespace backend  
❌ **Comments**: Comment systems require backend support  
❌ **Dynamic Content**: Any content that was dynamically loaded from Squarespace won't work

## Quick Start

### Option 1: Python HTTP Server (Recommended)

```bash
# Python 3
python3 server.py

# Or use built-in server
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

### Option 2: Node.js HTTP Server

```bash
# Install http-server globally
npm install -g http-server

# Run server
http-server -p 8000
```

### Option 3: PHP Built-in Server

```bash
php -S localhost:8000
```

### Option 4: Any Static Host

You can deploy this to any static hosting service:
- **Netlify**: Drag and drop the folder
- **Vercel**: `vercel deploy`
- **GitHub Pages**: Push to a repository and enable Pages
- **Apache/Nginx**: Copy files to web root

## File Structure

```
.
├── index.html              # Homepage
├── about.html              # About page
├── services.html           # Services page
├── gallery.html            # Gallery page
├── contact-5.html          # Contact page
├── book-a-consultation.html
├── cart.html               # Cart (non-functional without backend)
├── our-team.html
├── staging-service-policies.html
├── css/                    # Stylesheets
├── js/                     # JavaScript files
│   ├── rerouter.js        # URL remapping (important!)
│   └── ...                # Other JS files
├── images/                 # Image assets
├── server.py               # Python server script
└── README.md              # This file
```

## Conversion Script

If you need to reconvert the site, run:

```bash
python3 convert-to-static.py
```

This will:
- Remove external Squarespace CDN links
- Remove "Made with Squarespace" badges
- Clean up HTML files

## Notes

1. **Fonts**: The site uses Adobe Typekit fonts. These require an internet connection to load. If you want to make it fully offline, you'll need to:
   - Download the fonts
   - Host them locally
   - Update the font references in CSS

2. **Google Analytics**: The site includes Google Analytics tracking. This is preserved and will work if you have a valid GA ID.

3. **Images**: All images are included locally in the `images/` directory.

4. **Forms**: To make forms work, you'll need to:
   - Set up a form backend (e.g., Formspree, Netlify Forms, or your own server)
   - Update form action URLs in the HTML files

5. **Cart**: The shopping cart page exists but won't process orders. You'll need to integrate with an e-commerce solution like:
   - Stripe Checkout
   - PayPal
   - Shopify Buy Button
   - Or build a custom backend

## Troubleshooting

**Images not loading?**
- Check that the `images/` directory exists and contains the image files
- Verify the `rerouter.js` is loaded and working

**Styles not applying?**
- Ensure CSS files are in the `css/` directory
- Check browser console for 404 errors

**JavaScript errors?**
- Some Squarespace-specific JavaScript may fail gracefully
- Check browser console for specific errors
- The site should still display static content even if some JS fails

## License

This is a converted Squarespace export. The content and design belong to Amber Modern. This conversion is for self-hosting purposes only.

