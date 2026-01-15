// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
	output: 'static',
	adapter: cloudflare(),
	site: 'https://comfyui-error-db.pages.dev',
	integrations: [mdx(), sitemap()],
});
