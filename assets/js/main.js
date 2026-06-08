
        console.log("Start Akademie Elite-Portal Initializing...");

        document.addEventListener('DOMContentLoaded', () => {

            // Safe Lucide initialization
            try {
                if (typeof lucide !== 'undefined') {
                    lucide.createIcons();
                    console.log("Lucide Icons initialized.");
                } else {
                    console.warn("Lucide library not loaded.");
                }
            } catch(e) {
                console.error("Lucide setup failed:", e);
            }

            // Safe Lenis smooth scroll initialization
            let lenis = null;
            try {
                if (typeof Lenis !== 'undefined') {
                    lenis = new Lenis({ lerp: 0.08, smoothWheel: true });
                    if (typeof ScrollTrigger !== 'undefined') {
                        lenis.on('scroll', ScrollTrigger.update);
                    }
                    if (typeof gsap !== 'undefined') {
                        gsap.ticker.add((time) => lenis.raf(time * 1000));
                        gsap.ticker.lagSmoothing(0);
                    }
                    console.log("Lenis Smooth Scroll active.");
                } else {
                    console.warn("Lenis library not loaded.");
                }
            } catch (e) {
                console.error("Lenis setup failed:", e);
            }

            // Safe GSAP registration
            try {
                if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
                    gsap.registerPlugin(ScrollTrigger);
                    console.log("GSAP ScrollTrigger registered.");
                }
            } catch (e) {
                console.error("GSAP setup failed:", e);
            }

            // Dynamic Copyright Year
            const yearSpan = document.getElementById('copyright-year');
            if (yearSpan) yearSpan.textContent = new Date().getFullYear();

            /* --- IMMERSIVE 3D WEBGL FLIGHT JOURNEY SCENE --- */
            // Immersive 3D Game variables
            let isGameActive = false;
            let moveForward = false;
            let moveBackward = false;
            let moveLeft = false;
            let moveRight = false;
            
            let mouseX = 0;
            let mouseY = 0;
            let targetYaw = 0;
            let targetPitch = 0;
            let currentYaw = 0;
            let currentPitch = 0;

            const gameKeys = {
                w: false, a: false, s: false, d: false,
                ArrowUp: false, ArrowDown: false, ArrowLeft: false, ArrowRight: false
            };

            /* --- IMMERSIVE 3D WEBGL MULTI-CAMPUS EXPLORER (THREE.JS) --- */
            function initWebGLFlight() {
                try {
                    const canvas = document.getElementById('canvas-3d');
                    if (!canvas) return;

                    if (typeof THREE === 'undefined') {
                        console.warn("Three.js not loaded. Skipping 3D flight rendering.");
                        return;
                    }

                    let width = window.innerWidth;
                    let height = window.innerHeight;

                    const scene = new THREE.Scene();
                    
                    // Perspective Camera
                    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
                    camera.position.set(0, 0.5, 18); // Walking eye level height

                    const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
                    renderer.setSize(width, height);
                    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

                    // LIGHTS
                    const ambientLight = new THREE.AmbientLight(0xffffff, 0.45);
                    scene.add(ambientLight);

                    const cyanLight = new THREE.PointLight(0x00f0ff, 2.5, 30);
                    cyanLight.position.set(-10, 5, -10);
                    scene.add(cyanLight);

                    const goldLight = new THREE.PointLight(0xc5a059, 2.5, 30);
                    goldLight.position.set(10, 5, -25);
                    scene.add(goldLight);

                    // CYBERNETIC CAMPUS FLOOR (GROUND)
                    const groundGrid = new THREE.GridHelper(120, 60, 0x00f0ff, 0x011a3b);
                    groundGrid.position.y = -2.5;
                    scene.add(groundGrid);

                    const groundGeom = new THREE.PlaneGeometry(120, 120);
                    const groundMat = new THREE.MeshBasicMaterial({
                        color: 0x010206,
                        transparent: true,
                        opacity: 0.9,
                        side: THREE.DoubleSide
                    });
                    const ground = new THREE.Mesh(groundGeom, groundMat);
                    ground.rotation.x = Math.PI / 2;
                    ground.position.y = -2.52;
                    scene.add(ground);

                    // Premium Solid semi-translucent materials
                    const goldWireMaterial = new THREE.MeshBasicMaterial({
                        color: 0xc5a059, // Gold
                        wireframe: false,
                        transparent: true,
                        opacity: 0.65
                    });

                    const cyanWireMaterial = new THREE.MeshBasicMaterial({
                        color: 0x00f0ff, // Cyan
                        wireframe: false,
                        transparent: true,
                        opacity: 0.4
                    });

                    const portalMaterial = new THREE.MeshBasicMaterial({
                        color: 0x00f0ff,
                        wireframe: false,
                        transparent: true,
                        opacity: 0.25,
                        blending: THREE.AdditiveBlending
                    });

                    // Texture Loader for Real University Visuals
                    const textureLoader = new THREE.TextureLoader();
                    const heidelbergTex = textureLoader.load('assets/heidelberg.png');
                    const tumTex = textureLoader.load('assets/tum.png');
                    const goetheTex = textureLoader.load('assets/goethe.png');

                    // Create basic materials using the textures
                    const heidelbergTexMat = new THREE.MeshBasicMaterial({
                        map: heidelbergTex,
                        side: THREE.DoubleSide,
                        transparent: true,
                        opacity: 0.9
                    });
                    const tumTexMat = new THREE.MeshBasicMaterial({
                        map: tumTex,
                        side: THREE.DoubleSide,
                        transparent: true,
                        opacity: 0.9
                    });
                    const goetheTexMat = new THREE.MeshBasicMaterial({
                        map: goetheTex,
                        side: THREE.DoubleSide,
                        transparent: true,
                        opacity: 0.9
                    });

                    // 3D ENVIRONMENT 1: HEIDELBERG NEOCLASSICAL COLONNADE COURT
                    const heidelbergGroup = new THREE.Group();
                    scene.add(heidelbergGroup);

                    // Left & Right Colonnades
                    const columnGeom = new THREE.CylinderGeometry(0.15, 0.18, 5, 8);
                    const columnCount = 10;
                    for (let i = 0; i < columnCount; i++) {
                        const zPos = 15 - i * 6; // Spacing along corridor
                        
                        // Left column
                        const colL = new THREE.Mesh(columnGeom, goldWireMaterial);
                        colL.position.set(-6, 0, zPos);
                        heidelbergGroup.add(colL);

                        // Right column
                        const colR = new THREE.Mesh(columnGeom, goldWireMaterial);
                        colR.position.set(6, 0, zPos);
                        heidelbergGroup.add(colR);
                    }

                    // Neoclassical University Main Facade Gate (Heidelberg Entrance)
                    const portalGroup = new THREE.Group();
                    portalGroup.position.set(0, 0, 12);
                    heidelbergGroup.add(portalGroup);

                    // Columns
                    for(let i = 0; i < 4; i++) {
                        const col = new THREE.Mesh(columnGeom, goldWireMaterial);
                        col.position.x = (i - 1.5) * 2;
                        portalGroup.add(col);
                    }
                    // Plinth
                    const plinth = new THREE.Mesh(new THREE.BoxGeometry(7.5, 0.4, 1.5), goldWireMaterial);
                    plinth.position.y = -2.5;
                    portalGroup.add(plinth);
                    // Pediment (Roof)
                    const roof = new THREE.Mesh(new THREE.ConeGeometry(4.5, 1.5, 4), goldWireMaterial);
                    roof.rotation.y = Math.PI / 4;
                    roof.position.y = 3.25;
                    portalGroup.add(roof);

                    // Heidelberg Real University Photo Billboard inside 3D Archway
                    const heidelbergBillboard = new THREE.Mesh(new THREE.PlaneGeometry(8, 4.5), heidelbergTexMat);
                    heidelbergBillboard.position.set(0, 0.5, 11.5); // Positioned directly inside the neoclassical column archway
                    heidelbergGroup.add(heidelbergBillboard);

                    // 3D ENVIRONMENT 2: TU MÜNCHEN (TUM) CYBERNETIC HALL
                    const tumGroup = new THREE.Group();
                    tumGroup.position.set(0, 0, -25);
                    scene.add(tumGroup);

                    // Cybernetic Solar Pavilion
                    const pavilionGeom = new THREE.IcosahedronGeometry(4.5, 2);
                    const pavilion = new THREE.Mesh(pavilionGeom, cyanWireMaterial);
                    pavilion.position.set(0, 2, 0);
                    tumGroup.add(pavilion);

                    // Tech columns
                    const techColumnGeom = new THREE.BoxGeometry(0.3, 5, 0.3);
                    for(let i = 0; i < 6; i++) {
                        const angle = (i / 6) * Math.PI * 2;
                        const r = 8;
                        const col = new THREE.Mesh(techColumnGeom, cyanWireMaterial);
                        col.position.set(Math.cos(angle) * r, 0, Math.sin(angle) * r);
                        tumGroup.add(col);
                    }

                    // TUM Real University Photo Billboard inside 3D Cybernetic Hall
                    const tumBillboard = new THREE.Mesh(new THREE.PlaneGeometry(8, 4.5), tumTexMat);
                    tumBillboard.position.set(0, 1.5, -2); // Positioned inside the cybernetic pavilion
                    tumGroup.add(tumBillboard);

                    // 3D ENVIRONMENT 3: HUMBOLDT BERLIN SPEECH WAVES (Particles)
                    const starsCount = 400;
                    const starPositions = new Float32Array(starsCount * 3);
                    const starColors = new Float32Array(starsCount * 3);
                    const colorCyan = new THREE.Color('#00f0ff');
                    const colorGold = new THREE.Color('#c5a059');

                    for(let i = 0; i < starsCount; i++) {
                        starPositions[i*3] = (Math.random() - 0.5) * 60;
                        starPositions[i*3+1] = -2.5 + Math.random() * 15;
                        starPositions[i*3+2] = -15 - Math.random() * 60;

                        const clr = Math.random() > 0.5 ? colorCyan : colorGold;
                        starColors[i*3] = clr.r;
                        starColors[i*3+1] = clr.g;
                        starColors[i*3+2] = clr.b;
                    }
                    const starGeo = new THREE.BufferGeometry();
                    starGeo.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
                    starGeo.setAttribute('color', new THREE.BufferAttribute(starColors, 3));

                    // Dynamic Texture for particles
                    const pCanvas = document.createElement('canvas');
                    pCanvas.width = 16;
                    pCanvas.height = 16;
                    const pCtx = pCanvas.getContext('2d');
                    const grad = pCtx.createRadialGradient(8, 8, 0, 8, 8, 8);
                    grad.addColorStop(0, 'rgba(255,255,255,1)');
                    grad.addColorStop(0.3, 'rgba(255,255,255,0.8)');
                    grad.addColorStop(1, 'rgba(255,255,255,0)');
                    pCtx.fillStyle = grad;
                    pCtx.fillRect(0, 0, 16, 16);
                    const pTexture = new THREE.CanvasTexture(pCanvas);

                    const starMat = new THREE.PointsMaterial({
                        size: 0.25,
                        vertexColors: true,
                        map: pTexture,
                        transparent: true,
                        opacity: 0.85,
                        blending: THREE.AdditiveBlending,
                        depthWrite: false
                    });
                    const starField = new THREE.Points(starGeo, starMat);
                    scene.add(starField);

                    // 3D ENVIRONMENT 3: GOETHE FRANKFURT CAMPUS (NEW 3D PORTAL)
                    const goetheGroup = new THREE.Group();
                    goetheGroup.position.set(0, 0, -65);
                    scene.add(goetheGroup);

                    // Goethe Classical Archway columns
                    for (let i = 0; i < 2; i++) {
                        const col = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.25, 6, 12), goldWireMaterial);
                        col.position.set(i === 0 ? -4 : 4, 0.5, 0);
                        goetheGroup.add(col);
                    }
                    const goetheBeam = new THREE.Mesh(new THREE.BoxGeometry(9, 0.5, 1.2), goldWireMaterial);
                    goetheBeam.position.set(0, 3.5, 0);
                    goetheGroup.add(goetheBeam);

                    // Goethe Real University Photo Billboard inside 3D Archway
                    const goetheBillboard = new THREE.Mesh(new THREE.PlaneGeometry(8, 4.5), goetheTexMat);
                    goetheBillboard.position.set(0, 0.5, -0.5);
                    goetheGroup.add(goetheBillboard);

                    // FLOATING RESEARCH NODES & MATH CLUSTERS (Interactive)
                    const researchNodes = [];
                    const nodeGeoms = [
                        new THREE.OctahedronGeometry(0.4),
                        new THREE.TorusGeometry(0.3, 0.08, 6, 16),
                        new THREE.IcosahedronGeometry(0.35, 0)
                    ];
                    
                    for (let i = 0; i < 15; i++) {
                        const geom = nodeGeoms[i % nodeGeoms.length];
                        const mat = (i % 2 === 0) ? goldWireMaterial : cyanWireMaterial;
                        const mesh = new THREE.Mesh(geom, mat);
                        
                        mesh.position.set(
                            (Math.random() - 0.5) * 10,
                            -1 + Math.random() * 4,
                            15 - Math.random() * 50
                        );
                        scene.add(mesh);
                        researchNodes.push(mesh);
                    }

                    // Render loop
                    const clock = new THREE.Clock();
                    function animate() {
                        requestAnimationFrame(animate);
                        const elapsedTime = clock.getElapsedTime();

                        // Dynamic idle animations for environmental groups
                        pavilion.rotation.y = elapsedTime * 0.15;
                        pavilion.rotation.z = Math.sin(elapsedTime * 0.2) * 0.2;
                        
                        portalGroup.position.y = Math.sin(elapsedTime * 0.5) * 0.08;

                        researchNodes.forEach((node, idx) => {
                            node.rotation.x = elapsedTime * (0.2 + (idx * 0.03));
                            node.rotation.y = elapsedTime * (0.3 + (idx * 0.02));
                            node.position.y += Math.sin(elapsedTime + idx) * 0.003;
                        });

                        // 3D GAME MODE MOVEMENT & PHYSICS
                        if (isGameActive) {
                            // Lerp yaw and pitch for smooth rotation look
                            currentYaw += (targetYaw - currentYaw) * 0.1;
                            currentPitch += (targetPitch - currentPitch) * 0.1;

                            camera.rotation.set(0, 0, 0); // Reset
                            camera.rotation.y = currentYaw;
                            camera.rotation.x = currentPitch;

                            // Calculate keyboard movement vector
                            const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(camera.quaternion);
                            forward.y = 0; // Stick to flat ground plane
                            forward.normalize();

                            const right = new THREE.Vector3(1, 0, 0).applyQuaternion(camera.quaternion);
                            right.y = 0;
                            right.normalize();

                            const speed = 0.18;
                            
                            if (gameKeys.w || gameKeys.ArrowUp) camera.position.addScaledVector(forward, speed);
                            if (gameKeys.s || gameKeys.ArrowDown) camera.position.addScaledVector(forward, -speed);
                            if (gameKeys.a || gameKeys.ArrowLeft) camera.position.addScaledVector(right, -speed);
                            if (gameKeys.d || gameKeys.ArrowRight) camera.position.addScaledVector(right, speed);

                            // Collisions / Boundaries (Keep user inside the beautiful campus corridor)
                            camera.position.x = Math.max(-20, Math.min(20, camera.position.x));
                            camera.position.z = Math.max(-80, Math.min(22, camera.position.z));
                            camera.position.y = 0.5; // Stay at realistic human walk height

                            // Update HUD Radar / Minimap Player blip location
                            const radarPlayer = document.getElementById('radar-player');
                            if (radarPlayer) {
                                const percentX = (camera.position.x - (-20)) / 40;
                                const percentZ = (camera.position.z - (-60)) / 82;
                                radarPlayer.style.left = (15 + percentX * 90) + 'px';
                                radarPlayer.style.top = (15 + percentZ * 90) + 'px';
                            }

                            // Dynamic compass readouts
                            const hudDirection = document.getElementById('hud-direction');
                            if (hudDirection) {
                                let zone = "CAMPUS COURTYARD";
                                if (camera.position.z > 5) zone = "HEIDELBERG COLONNADE";
                                else if (camera.position.z < -15) zone = "TU MÜNCHEN DIGITAL PLATFORM";
                                hudDirection.textContent = `LOC: X: ${camera.position.x.toFixed(1)} Z: ${camera.position.z.toFixed(1)} | ${zone}`;
                            }
                        } else {
                            // SCROLL STORYTELLING MODE: Camera rotation is idle parallax
                            camera.rotation.x = 0;
                            camera.rotation.y = 0;
                            camera.rotation.z = 0;
                        }

                        renderer.render(scene, camera);
                    }
                    animate();

                    // GSAP ScrollTrigger Flight Timeline (Activated only when NOT in game mode)
                    let scrollTimeline = null;
                    function setupScrollTimeline() {
                        if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
                            scrollTimeline = gsap.timeline({
                                scrollTrigger: {
                                    trigger: "body",
                                    start: "top top",
                                    end: "bottom bottom",
                                    scrub: 1.2,
                                    onUpdate: (self) => {
                                        if (isGameActive) return; // Do not overwrite if playing
                                        
                                        // Standard storytelling flight positions
                                        const progress = self.progress;
                                        camera.position.z = 18 - progress * 85; // Zooms all the way past Goethe
                                        camera.position.x = Math.sin(progress * Math.PI * 2) * 2;
                                        camera.position.y = 0.5 + Math.cos(progress * Math.PI) * 0.8;
                                        
                                        // Slow rotating corridor perspective
                                        camera.rotation.y = Math.sin(progress * Math.PI) * 0.25;
                                    }
                                }
                            });
                        }
                    }
                    setupScrollTimeline();

                    // Event Listeners for 3D Game controls
                    window.addEventListener('keydown', (e) => {
                        if (!isGameActive) return;
                        if (e.key === 'Escape' || e.key === 'Esc') {
                            exit3DGameMode();
                            return;
                        }
                        const key = e.key.toLowerCase();
                        if (key in gameKeys) gameKeys[key] = true;
                        if (e.key in gameKeys) gameKeys[e.key] = true;
                    });

                    window.addEventListener('keyup', (e) => {
                        const key = e.key.toLowerCase();
                        if (key in gameKeys) gameKeys[key] = false;
                        if (e.key in gameKeys) gameKeys[e.key] = false;
                    });

                    // Mouse Drag/Move to Look rotation math
                    let isDragging = false;
                    window.addEventListener('mousedown', () => { isDragging = true; });
                    window.addEventListener('mouseup', () => { isDragging = false; });
                    
                    window.addEventListener('mousemove', (e) => {
                        if (!isGameActive) return;
                        
                        // Intuitive Drag-to-Look on click, or mouse-center offset
                        const centerX = window.innerWidth / 2;
                        const centerY = window.innerHeight / 2;
                        
                        targetYaw = - (e.clientX - centerX) * 0.0028;
                        targetPitch = - (e.clientY - centerY) * 0.002;
                        
                        // Limit vertical look angle (pitch limit) to avoid camera flipping upside down
                        targetPitch = Math.max(-Math.PI / 4, Math.min(Math.PI / 4, targetPitch));
                    });

                    // Touch Drag to look (Mobile support!)
                    window.addEventListener('touchmove', (e) => {
                        if (!isGameActive) return;
                    });
                    // Resize handler
                    window.addEventListener('resize', () => {
                        width = window.innerWidth;
                        height = window.innerHeight;
                        camera.aspect = width / height;
                        camera.updateProjectionMatrix();
                        renderer.setSize(width, height);
                    });

                    console.log("3D Immersive Multi-Campus Explorer Engine loaded successfully.");
                } catch(err) {
                    console.error("Critical error in 3D WebGL initialization:", err);
                }
            }
            
            // Trigger 3D init
            initWebGLFlight();

            /* --- 3D GAME MODE ACTIVATION TRIGGERS --- */
            const btnStartGame = document.getElementById('btn-start-3d-game');
            const btnExitGame = document.getElementById('btn-exit-3d-game');
            const gameHudOverlay = document.getElementById('game-hud-overlay');

            function enter3DGameMode() {
                isGameActive = true;
                const canvas = document.getElementById('canvas-3d');
                if (canvas) canvas.style.display = 'block';
                document.body.classList.add('game-lock');
                if (gameHudOverlay) gameHudOverlay.classList.add('active');
                if (typeof lenis !== 'undefined' && lenis) {
                    lenis.stop();
                }
            }

            function exit3DGameMode() {
                isGameActive = false;
                const canvas = document.getElementById('canvas-3d');
                if (canvas) canvas.style.display = 'none';
                document.body.classList.remove('game-lock');
                if (gameHudOverlay) gameHudOverlay.classList.remove('active');
                
                // Clear active keys
                for (let key in gameKeys) gameKeys[key] = false;
                if (typeof lenis !== 'undefined' && lenis) {
                    lenis.start();
                }
            }

            if (btnStartGame) btnStartGame.addEventListener('click', enter3DGameMode);
            if (btnExitGame) btnExitGame.addEventListener('click', exit3DGameMode);

            /* --- HYLIOX-STYLE SCROLL GATE GSAP TIMELINE --- */
            if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
                gsap.registerPlugin(ScrollTrigger);

                const gateTl = gsap.timeline({
                    scrollTrigger: {
                        trigger: ".scroll-gate-section",
                        start: "top top",
                        end: "bottom bottom",
                        scrub: 1
                    }
                });

                // 1. Fade out initial content
                gateTl.to(".gate-initial-hero", { opacity: 0, y: -80, pointerEvents: "none", ease: "power1.inOut" }, 0.2)
                      .to(".scroll-indicator-mouse", { opacity: 0, ease: "power1.inOut" }, 0.2);

                // 2. Animate Slide 1 (Welcome) in and out
                gateTl.to("#slide-welcome", { opacity: 1, y: 0, pointerEvents: "auto", duration: 1.5 }, 0.8)
                      .to("#slide-welcome", { opacity: 0, y: -60, pointerEvents: "none", duration: 1.5 }, 2.5);

                // 3. Animate Slide 2 (Bridge) in and out
                gateTl.to("#slide-bridge", { opacity: 1, y: 0, pointerEvents: "auto", duration: 1.5 }, 2.8)
                      .to("#slide-bridge", { opacity: 0, y: -60, pointerEvents: "none", duration: 1.5 }, 4.5);
            }

            /* --- FLOATING AUTOHIDE GLASS NAVBAR --- */
            const navbar = document.getElementById('navbar');
            let lastScrollY = window.scrollY;

            window.addEventListener('scroll', () => {
                if (window.scrollY > 50) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }

                if (window.scrollY > lastScrollY && window.scrollY > 120) {
                    navbar.classList.add('hidden');
                } else {
                    navbar.classList.remove('hidden');
                }
                lastScrollY = window.scrollY;
            });

            /* --- MOBILE MENU PANEL --- */
            const mobileToggleBtn = document.getElementById('mobile-toggle-btn');
            const mobileMenuPanel = document.getElementById('mobile-menu-panel');

            if (mobileToggleBtn && mobileMenuPanel) {
                mobileToggleBtn.addEventListener('click', () => {
                    mobileMenuPanel.classList.toggle('active');
                    const isActive = mobileMenuPanel.classList.contains('active');
                    mobileToggleBtn.innerHTML = isActive ? '<i data-lucide="x"></i>' : '<i data-lucide="menu"></i>';
                    try { lucide.createIcons(); } catch(e) {}
                });

                mobileMenuPanel.querySelectorAll('a').forEach(item => {
                    item.addEventListener('click', () => {
                        mobileMenuPanel.classList.remove('active');
                        mobileToggleBtn.innerHTML = '<i data-lucide="menu"></i>';
                        try { lucide.createIcons(); } catch(e) {}
                    });
                });
            }

            /* --- GSAP ANIMATION PRESETS: PANEL REVEALS --- */
            if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
                gsap.utils.toArray('.glass-panel, .card').forEach(el => {
                    gsap.fromTo(el, 
                        { opacity: 0, y: 50 },
                        { 
                            opacity: 1, 
                            y: 0, 
                            duration: 1.4, 
                            ease: 'power4.out',
                            scrollTrigger: {
                                trigger: el,
                                start: 'top 85%',
                                toggleActions: 'play none none none'
                            }
                        }
                    );
                });

                /* --- MAGNETIC HOVER BUTTONS --- */
                document.querySelectorAll('.btn-magnetic').forEach(btn => {
                    btn.addEventListener('mousemove', (e) => {
                        const rect = btn.getBoundingClientRect();
                        const x = e.clientX - rect.left - rect.width / 2;
                        const y = e.clientY - rect.top - rect.height / 2;
                        gsap.to(btn, { x: x * 0.25, y: y * 0.25, duration: 0.3, ease: 'power2.out' });
                    });
                    btn.addEventListener('mouseleave', () => {
                        gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.3)' });
                    });
                });

                /* --- 3D CARD PERSPECTIVE TILT --- */
                document.querySelectorAll('.card, .pkg-card').forEach(card => {
                    card.addEventListener('mousemove', (e) => {
                        const rect = card.getBoundingClientRect();
                        const x = e.clientX - rect.left;
                        const y = e.clientY - rect.top;
                        
                        const xc = rect.width / 2;
                        const yc = rect.height / 2;
                        
                        const angleX = (yc - y) / 16;
                        const angleY = (x - xc) / 16;
                        
                        gsap.to(card, {
                            rotateX: angleX,
                            rotateY: angleY,
                            duration: 0.3,
                            ease: 'power2.out'
                        });
                    });

                    card.addEventListener('mouseleave', () => {
                        gsap.to(card, {
                            rotateX: 0,
                            rotateY: 0,
                            duration: 0.5,
                            ease: 'power2.out'
                        });
                    });
                });
            }

            /* --- SPERRKONTO COST SIMULATOR --- */
            const sliderMonthsInput = document.getElementById('slider-months-input');
            const sliderMonthsDisplay = document.getElementById('slider-months-display');
            const chkBwInput = document.getElementById('chk-bw-input');
            const bwRowDisplay = document.getElementById('bw-row-display');
            const legendBwItem = document.getElementById('legend-bw-item');

            const valSperrkonto = document.getElementById('val-sperrkonto');
            const valBw = document.getElementById('val-bw');
            const valTotal = document.getElementById('val-total');
            const visualProgressBar = document.getElementById('visual-progress-bar');

            function formatCurrency(val) {
                return val.toLocaleString('de-DE') + ' €';
            }

            function updateBudgetCalculator() {
                if (!sliderMonthsInput) return;
                const months = parseInt(sliderMonthsInput.value);
                sliderMonthsDisplay.textContent = months + ' Ay';

                const sperrkontoAmount = months * 992;
                valSperrkonto.textContent = formatCurrency(sperrkontoAmount);

                const visaFee = 75;
                const assistFee = 75;
                const totalFees = visaFee + assistFee;

                let bwTax = 0;
                if (chkBwInput && chkBwInput.checked) {
                    bwRowDisplay.style.display = 'flex';
                    legendBwItem.style.display = 'inline-flex';
                    const semesters = Math.ceil(months / 6);
                    bwTax = semesters * 1500;
                    valBw.textContent = formatCurrency(bwTax);
                } else {
                    bwRowDisplay.style.display = 'none';
                    legendBwItem.style.display = 'none';
                }

                const totalAmount = sperrkontoAmount + totalFees + bwTax;
                valTotal.textContent = formatCurrency(totalAmount);

                if (visualProgressBar) {
                    const pctSperrkonto = (sperrkontoAmount / totalAmount) * 100;
                    const pctBw = (bwTax / totalAmount) * 100;
                    const pctFees = (totalFees / totalAmount) * 100;

                    visualProgressBar.querySelector('.bar-sperrkonto').style.width = pctSperrkonto + '%';
                    visualProgressBar.querySelector('.bar-bw').style.width = pctBw + '%';
                    visualProgressBar.querySelector('.bar-fees').style.width = pctFees + '%';
                }
            }

            if (sliderMonthsInput) {
                sliderMonthsInput.addEventListener('input', updateBudgetCalculator);
            }
            if (chkBwInput) {
                chkBwInput.addEventListener('change', updateBudgetCalculator);
            }
            updateBudgetCalculator(); // Init calculation

            /* --- BuT ELIGIBILITY WIZARD --- */
            const butYes1 = document.getElementById('but-yes-1');
            const butNo1 = document.getElementById('but-no-1');
            const butYes2 = document.getElementById('but-yes-2');
            const butNo2 = document.getElementById('but-no-2');

            const butStep1 = document.getElementById('but-step-1');
            const butStep2 = document.getElementById('but-step-2');
            const butResultSuccess = document.getElementById('but-result-success');
            const butResultFail = document.getElementById('but-result-fail');

            if (butYes1 && butNo1 && butStep1) {
                butYes1.addEventListener('click', () => {
                    butStep1.classList.remove('active');
                    butStep2.classList.add('active');
                });
                butNo1.addEventListener('click', () => {
                    butStep1.classList.remove('active');
                    butResultFail.classList.add('active');
                });
            }

            if (butYes2 && butNo2 && butStep2) {
                butYes2.addEventListener('click', () => {
                    butStep2.classList.remove('active');
                    butResultSuccess.classList.add('active');
                });
                butNo2.addEventListener('click', () => {
                    butStep2.classList.remove('active');
                    butResultFail.classList.add('active');
                });
            }

            /* --- ACTION FLOW MODALS --- */
            const actionModal = document.getElementById('action-modal');
            const modalTitleLbl = document.getElementById('modal-title-lbl');
            const modalBodyContent = document.getElementById('modal-body-content');
            const modalCloseBtn = document.getElementById('modal-close-btn');

            const btnShowEtutStepsModal = document.getElementById('btn-show-etut-steps-modal');
            const btnButSuccessCta = document.getElementById('btn-but-success-cta');

            function showModal(title, steps) {
                modalTitleLbl.textContent = title;
                modalBodyContent.innerHTML = '';
                const stepsFlowDiv = document.createElement('div');
                stepsFlowDiv.className = 'steps-flow';

                steps.forEach((step, index) => {
                    const stepDiv = document.createElement('div');
                    stepDiv.className = 'flow-step';
                    stepDiv.innerHTML = `
                        <div class="flow-num">${index + 1}</div>
                        <div>
                            <h4>${step.title}</h4>
                            <p>${step.desc}</p>
                        </div>
                    `;
                    stepsFlowDiv.appendChild(stepDiv);
                });
                modalBodyContent.appendChild(stepsFlowDiv);
                actionModal.classList.add('active');
            }

            if (btnShowEtutStepsModal && actionModal && modalCloseBtn) {
                btnShowEtutStepsModal.addEventListener('click', () => {
                    showModal('6 Adımda Ödev Etüt Takip Süreci', [
                        { title: 'Ankommen (Varış)', desc: 'Çocuğunuz belirlenen etüt saatlerinde Rüsselsheim merkezimize giriş yapar.' },
                        { title: 'Selbstständig arbeiten (Bağımsız Çalışma)', desc: 'Ödevler odaklanmış sınıfta bireysel çözülmeye başlar.' },
                        { title: 'Unterstützung (Destek)', desc: 'Eğitmenlerimiz takıldığı yerleri açıklar ve soruları pedagojik yaklaşımla anlatır.' },
                        { title: 'Kontrolle (Kontrol)', desc: 'Ödevlerin eksiksizliği ve doğruluğu eğitmenlerimizce tek tek incelenip onaylanır.' },
                        { title: 'Fertig? (Bitti mi?)', desc: 'Tüm ödevler bittiğinde çocuk veli bilgisi dahilinde güvenle uğurlanır.' },
                        { title: 'Keine Hausaufgaben? (Ödev Yoksa?)', desc: 'Ödevsiz günlerde kitap okuma, test yaprakları veya zeka oyunları ile vakit verimli değerlendirilir.' }
                    ]);
                });

                if (btnButSuccessCta) {
                    btnButSuccessCta.addEventListener('click', () => {
                        showModal('6 Adımda Ücretsiz BuT Nachhilfe Başvurusu', [
                            { title: 'Belge Talebi', desc: 'Start Akademie merkezimizden okul onay formu da dahil olmak üzere BuT başvuru formlarını talep edin.' },
                            { title: 'Formu Doldurma', desc: 'Velisi olarak çocuğunuzun ve kendinizin kurumsal bilgilerini formda eksiksiz doldurun.' },
                            { title: 'Okul Onayı (Lernförderung Bedarf)', desc: 'Sınıf öğretmeni veya okul yönetimi, çocuğun bu ders desteğine ihtiyacı olduğunu onaylayarak formu imzalar.' },
                            { title: 'Jobcenter / Sozialamt Gönderimi', desc: 'İmzalı ve onaylı evrakları bağlı bulunduğunuz yetkili sosyal yardım dairesine iletin.' },
                            { title: 'Onay Belgesi (Bewilligung)', desc: 'Sosyal daire başvurunuzu inceler ve %100 devlet onay belgesini posta yoluyla adresinize gönderir.' },
                            { title: 'Ücretsiz Kayıt', desc: 'Bu onay belgesiyle Start Akademie\'ye gelin, derslerimize tamamen ücretsiz başlayın! Ödemeyi doğrudan devlet yapar.' }
                        ]);
                    });
                }

                modalCloseBtn.addEventListener('click', () => {
                    actionModal.classList.remove('active');
                });

                actionModal.addEventListener('click', (e) => {
                    if (e.target === actionModal) {
                        actionModal.classList.remove('active');
                    }
                });
            }

            /* --- BOOKING DATE/TIME PICKERS --- */
            const dayPickerCards = document.querySelectorAll('#day-picker-cards .picker-card');
            const timePickerCards = document.querySelectorAll('#time-picker-cards .time-picker-card');

            dayPickerCards.forEach(card => {
                card.addEventListener('click', () => {
                    dayPickerCards.forEach(c => c.classList.remove('active'));
                    card.classList.add('active');
                });
            });

            timePickerCards.forEach(card => {
                card.addEventListener('click', () => {
                    timePickerCards.forEach(c => c.classList.remove('active'));
                    card.classList.add('active');
                });
            });

            /* --- STARTBOT CHATBOT LOGIC --- */
            const startbotToggleBtn = document.getElementById('startbot-toggle-btn');
            const startbotPanel = document.getElementById('startbot-panel');
            const startbotCloseBtn = document.getElementById('startbot-close-btn');

            const startbotTxtInput = document.getElementById('startbot-txt-input');
            const startbotSendBtn = document.getElementById('startbot-send-btn');
            const startbotMessagesBox = document.getElementById('startbot-messages-box');
            const startbotQuickChips = document.querySelectorAll('#startbot-quick-chips .startbot-chip');

            if (startbotToggleBtn && startbotPanel && startbotCloseBtn) {
                startbotToggleBtn.addEventListener('click', () => {
                    startbotPanel.classList.toggle('active');
                });

                startbotCloseBtn.addEventListener('click', () => {
                    startbotPanel.classList.remove('active');
                });
            }

            function appendBotMessage(sender, text) {
                const msgDiv = document.createElement('div');
                msgDiv.className = `msg ${sender}`;
                msgDiv.textContent = text;
                startbotMessagesBox.appendChild(msgDiv);
                startbotMessagesBox.scrollTop = startbotMessagesBox.scrollHeight;
            }

            function botResponse(userMsg) {
                appendBotMessage('bot', 'Düşünüyorum...');
                const loader = startbotMessagesBox.lastChild;

                setTimeout(() => {
                    if (loader) loader.remove();
                    const text = userMsg.toLowerCase();

                    if (text.includes('but') || text.includes('ücretsiz') || text.includes('sosyal') || text.includes('devlet')) {
                        appendBotMessage('bot', 'Almanya\'da Bürgergeld, Wohngeld veya Kinderzuschlag alan aileler için ders desteği tamamen ücretsizdir (BuT)! Form hazırlıklarınızı biz yönetiyoruz.');
                    } else if (text.includes('bloke') || text.includes('sperrkonto') || text.includes('bütçe') || text.includes('maliyet')) {
                        appendBotMessage('bot', 'Öğrenci vizesi için zorunlu bloke hesap bütçesi aylık 992 € (yıllık 11.904 €) düzeyindedir. Vize harcı ise 75 €\'dur. Sayfamızdaki akıllı simülatör ile detayları inceleyebilirsiniz.');
                    } else if (text.includes('sommercamp') || text.includes('kamp') || text.includes('hazırlık') || text.includes('abitur')) {
                        appendBotMessage('bot', 'Yaz 2026 Abitur ve İngilizce Sommercamp kayıtlarımız başlamıştır. Kontenjanlar dolmadan hızlıca randevu alabilirsiniz.');
                    } else if (text.includes('danışmanlık') || text.includes('paket') || text.includes('ücret') || text.includes('fiyat')) {
                        appendBotMessage('bot', 'Almanya üniversite danışmanlığımızda 3 paketimiz bulunur: Start Basic (1.900 €), Start Plus (2.700 €) ve Start Premium (3.900 € - 6 ay Almanya yerinde entegrasyon desteği içerir).');
                    } else {
                        appendBotMessage('bot', 'Sorunuz için teşekkürler! Size vize bloke hesabı, ücretsiz BuT okul desteği veya Sommercamp ders takvimlerimizle ilgili konularda daha detaylı yardımcı olmak için heyecan duyuyoruz. Lütfen randevu formumuzu doldurun.');
                    }
                }, 800);
            }

            function handleSend() {
                const txt = startbotTxtInput.value.trim();
                if (!txt) return;

                appendBotMessage('user', txt);
                startbotTxtInput.value = '';
                botResponse(txt);
            }

            if (startbotSendBtn && startbotTxtInput) {
                startbotSendBtn.addEventListener('click', handleSend);
                startbotTxtInput.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') handleSend();
                });
            }

            startbotQuickChips.forEach(chip => {
                chip.addEventListener('click', () => {
                    const question = chip.getAttribute('data-question');
                    appendBotMessage('user', question);
                    botResponse(question);
                });
            });

        });
    