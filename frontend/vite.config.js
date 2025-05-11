import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],

  server: {
    allowedHosts: ['localhost',"0ee7-2a05-45c2-73f2-cc00-6105-41d4-2656-fd0e.ngrok-free.app", "*"],
    host: true,      
    port: 5173,
  },
})

