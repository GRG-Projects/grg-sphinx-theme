/**
 * This method introduces a click function to click the
 * underlying "a" tag for "li" element with toctree-l2 of the design.
 */
export const toctreeClick = () => {
  const toctreeSubtopics = document.querySelectorAll(
    ".toctree-wrapper li.toctree-l2"
  );

  toctreeSubtopics.forEach((toctreel2) => {
    const link = toctreel2.querySelector("a");
    toctreel2.addEventListener("click", () => {
      link.click();
    });
  });
};

export const gridCalculation = () => {
  const toctrees = document.querySelectorAll(".toctree-wrapper li.toctree-l1");

  toctrees.forEach((toctree) => {
    const containerWidth = toctree.clientWidth;
    const subtrees = toctree.querySelectorAll("li.toctree-l2 a");
    const subtreeContainer = toctree.querySelector("ul");

    let width = 0;
    let noOfElements = 0;
    const MAX_ELEMENTS = 3;

    for (let i = 0; i < Math.min(MAX_ELEMENTS, subtrees.length); i++) {
      // considering the padding applied
      width += subtrees[i].offsetWidth + 32;

      if (width > containerWidth) {
        break;
      } else {
        noOfElements++;
      }

      // considering the gap applied
      width += 16;
    }

    if (subtrees.length > 0) {
      subtreeContainer.classList.add(`grid-${noOfElements}`);
    }
  });
};
