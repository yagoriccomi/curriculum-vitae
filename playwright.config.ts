import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: 'e2e',
  reporter: process.env.CI ? 'github' : 'list',
  use: { baseURL: `http://localhost:4173${process.env.BASE_PATH ?? '/'}`, reducedMotion: 'reduce', colorScheme: 'dark' },
  webServer: { command: 'npx vite preview --port 4173 --strictPort', port: 4173, reuseExistingServer: !process.env.CI },
  // Baselines visuais só existem em Linux (CI em container); decisão 004.
  snapshotPathTemplate: '{testDir}/__screenshots__/{arg}-{platform}{ext}',
})
