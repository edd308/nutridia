// v19.7: sin cacheado offline temporal para garantizar actualizaciones.
self.addEventListener('install',()=>self.skipWaiting());self.addEventListener('activate',e=>e.waitUntil(self.registration.unregister()));
