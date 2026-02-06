// Slide titles/headings for each slide
const slideHeadings = {
    1: "1st Visit - Title",
    2: "1st Visit - Inventory",
    3: "1st Visit - Gallery",
    4: "2nd Visit - Title",
    5: "2nd Visit - Inventory",
    6: "2nd Visit - Seeds",
    7: "2nd Visit - Gallery Part 1",
    8: "2nd Visit - Gallery Part 2",
    9: "2nd Visit - Gallery Part 3",
    10: "2nd Visit - Gallery Part 4",
    11: "2nd Visit - Gallery Part 5",
    12: "2nd Visit - Gallery Part 6",
    13: "2nd Visit - Gallery Part 7",
    14: "2nd Visit - Videos Part 1",
    15: "2nd Visit - Videos Part 2"
};

// Function to update slide counter with heading
function updateSlideCounter(currentSlide, totalSlides) {
    const slideCounter = document.getElementById('slideCounter');
    const slideNum = currentSlide + 1;
    const heading = slideHeadings[slideNum] || `Slide ${slideNum}`;

    slideCounter.innerHTML = `
        <div style="font-size: 1.2rem; font-weight: 700;">${slideNum} / ${totalSlides}</div>
        <div style="font-size: 0.75rem; opacity: 0.8; margin-top: 2px;">${heading}</div>
    `;
}
