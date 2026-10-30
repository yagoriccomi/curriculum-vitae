import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

// ponytail: BASE_PATH=/curriculum-vitae/ até o domínio próprio (ticket 009); depois fica '/'.
export default defineConfig({
  base: process.env.BASE_PATH ?? '/',
  plugins: [react()],
  test: { environment: 'jsdom', include: ['src/**/*.test.tsx'] },
})
