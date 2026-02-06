// ===== PRESENTATION NAVIGATION SCRIPT =====

class PresentationController {
    constructor() {
        this.slides = document.querySelectorAll('.slide');
        this.totalSlides = this.slides.length;
        this.currentSlide = 0;

        this.prevBtn = document.getElementById('prevBtn');
        this.nextBtn = document.getElementById('nextBtn');
        this.progressFill = document.getElementById('progressFill');
        this.slideCounter = document.getElementById('slideCounter');
        this.video = document.getElementById('presentationVideo');

        this.totalSlides = 18;
        this.slideHeadings = {
            0: "Presentation Dashboard",
            1: "1st Visit Items Overview",
            2: "1st Visit Video",
            3: "1st Visit Gallery",
            4: "Inventory Partially",
            5: "Items Not Found",
            6: "Additional Items",
            7: "Field Video",
            8: "Additional Items (P2)",
            9: "Gallery Part 1",
            10: "Gallery Part 3",
            11: "Field Videos (P2)",
            12: "Additional Items (P3)",
            13: "Gallery Part 4",
            14: "Consolidated Gallery",
            15: "Vermi Compost Gallery",
            16: "Crops Sales & Receivable",
            17: "Other Sales Overview"
        };

        this.init();
    }

    init() {
        // Event Listeners
        this.prevBtn.addEventListener('click', () => this.previousSlide());
        this.nextBtn.addEventListener('click', () => this.nextSlide());

        // Keyboard Navigation
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') this.previousSlide();
            if (e.key === 'ArrowRight') this.nextSlide();
            if (e.key === 'Home') this.goToSlide(0);
            if (e.key === 'End') this.goToSlide(this.totalSlides - 1);
            if (e.key === 'Escape') closeZoom();
        });

        // Touch/Swipe Support
        let touchStartX = 0;
        let touchEndX = 0;

        document.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        });

        document.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            this.handleSwipe();
        });

        const handleSwipe = () => {
            if (touchEndX < touchStartX - 50) this.nextSlide();
            if (touchEndX > touchStartX + 50) this.previousSlide();
        };

        this.handleSwipe = handleSwipe;

        // Initialize first slide
        this.updatePresentation();
    }

    nextSlide() {
        if (this.currentSlide < this.totalSlides - 1) {
            this.currentSlide++;
            this.updatePresentation();
        }
    }

    previousSlide() {
        if (this.currentSlide > 0) {
            this.currentSlide--;
            this.updatePresentation();
        }
    }

    goToSlide(index) {
        if (index >= 0 && index < this.totalSlides) {
            this.currentSlide = index;
            this.updatePresentation();
        }
    }

    updatePresentation() {
        // Update slides
        this.slides.forEach((slide, index) => {
            if (index === this.currentSlide) {
                slide.classList.add('active');
            } else {
                slide.classList.remove('active');
            }
        });

        // Update progress bar
        const progress = ((this.currentSlide + 1) / this.totalSlides) * 100;
        this.progressFill.style.width = `${progress}%`;

        // Update slide counter with heading
        const slideNum = this.currentSlide + 1;
        const heading = this.slideHeadings[slideNum] || `Slide ${slideNum}`;
        this.slideCounter.innerHTML = `
            <div style="font-size: 1.2rem; font-weight: 700;">${slideNum} / ${this.totalSlides}</div>
            <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 2px;">${heading}</div>
        `;

        // Update navigation buttons
        this.prevBtn.disabled = this.currentSlide === 0;
        this.nextBtn.disabled = this.currentSlide === this.totalSlides - 1;

        // Pause video when leaving video slide (slide 3, index 2)
        if (this.video && this.currentSlide !== 2) {
            this.video.pause();
        }

        // Add animation class to current slide content
        const currentSlideContent = this.slides[this.currentSlide].querySelector('.slide-content');
        if (currentSlideContent) {
            currentSlideContent.style.animation = 'none';
            setTimeout(() => {
                currentSlideContent.style.animation = 'contentFadeIn 0.8s ease 0.2s both';
            }, 10);
        }
    }
}

// ===== IMAGE ZOOM FUNCTIONALITY =====
function zoomImage(element) {
    const modal = document.getElementById('zoomModal');
    const modalImg = document.getElementById('zoomedImage');
    const modalVideo = document.getElementById('zoomedVideo');
    const caption = document.getElementById('zoomCaption');

    const img = element.querySelector('img');
    const captionText = element.querySelector('.gallery-caption-compact');

    // Show image, hide video
    modalImg.style.display = 'block';
    modalVideo.style.display = 'none';

    modal.classList.add('active');
    modalImg.src = img.src;
    caption.textContent = captionText.textContent;

    // Prevent body scroll when modal is open
    document.body.style.overflow = 'hidden';
}

function closeZoom() {
    const modal = document.getElementById('zoomModal');
    const modalVideo = document.getElementById('zoomedVideo');

    modal.classList.remove('active');

    // Re-enable body scroll
    document.body.style.overflow = 'auto';

    // Pause video if it's playing in modal
    if (modalVideo) {
        modalVideo.pause();
    }
}

// ===== VIDEO ZOOM FUNCTIONALITY =====
function zoomVideo(element) {
    const modal = document.getElementById('zoomModal');
    const modalImg = document.getElementById('zoomedImage');
    const modalVideo = document.getElementById('zoomedVideo');
    const caption = document.getElementById('zoomCaption');

    const video = element.querySelector('video');
    // Try to find caption in parent or siblings
    const captionElement = element.parentElement.querySelector('.video-caption-compact') ||
        element.querySelector('.slide-title');

    // Hide image, show video
    modalImg.style.display = 'none';
    modalVideo.style.display = 'block';

    modal.classList.add('active');

    // Support both <source> and direct <video src>
    const source = video.querySelector('source');
    modalVideo.src = source ? source.src : video.src;

    if (captionElement) {
        caption.textContent = captionElement.textContent;
    } else {
        caption.textContent = "Video Gallery";
    }

    // Play video automatically
    modalVideo.play().catch(error => {
        console.log("Auto-play was prevented:", error);
    });

    // Prevent body scroll when modal is open
    document.body.style.overflow = 'hidden';
}

// Initialize presentation when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.presentation = new PresentationController();

    // Add smooth scroll behavior
    document.documentElement.style.scrollBehavior = 'smooth';

    // Preload images for better performance
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        const imgElement = new Image();
        imgElement.src = img.src;
    });

    // Add entrance animation
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

// Prevent context menu on presentation (optional)
document.addEventListener('contextmenu', (e) => {
    e.preventDefault();
});

// Add fullscreen toggle (F key)
document.addEventListener('keydown', (e) => {
    if (e.key === 'f' || e.key === 'F') {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen();
        } else {
            document.exitFullscreen();
        }
    }
});
