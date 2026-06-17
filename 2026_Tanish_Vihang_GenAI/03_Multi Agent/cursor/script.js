/**
 * EDIT YOUR ADVENTURE HERE
 * ------------------------
 * - Add scenes under STORY.scenes
 * - Point choices at scene ids with `next`
 * - Set START_SCENE to your opening scene id
 * - Endings use choices with next: null (or omit choices entirely)
 */
const STORY = {
  title: "Whispers from the Hollow",
  startScene: "intro",

  scenes: {
    intro: {
      title: "The Crossroads",
      text: `Rain hammers the cobblestones of Eldermoor. You clutch a torn map that promises a vault beneath the old cathedral—gold enough to erase every debt you owe.

Lightning splits the sky. Three paths lie before you.`,
      choices: [
        { label: "Sneak through the sewers", next: "sewers" },
        { label: "Knock on the cathedral doors", next: "cathedral" },
        // { label: "Follow the hooded stranger", next: "stranger" },
        { label: "Explore the forest", next: "forest" },
      ],
    },

    sewers: {
      title: "Beneath the City",
      text: `The sewers reek of rust and rot. Rats scatter as your lantern flickers. Ahead, you hear voices—guards, or something wearing their armor.

A ladder leads up toward the vault. A side tunnel glows faintly blue.`,
      choices: [
        { label: "Charge the voices", next: "fight" },
        { label: "Climb toward the vault", next: "vault" },
        { label: "Investigate the blue glow", next: "magic" },
      ],
    },

    cathedral: {
      title: "Holy Ground",
      text: `The doors creak open without resistance. Candles burn though no one tends them. A priest in silver robes watches you from the altar.

"Seeking fortune?" he asks. "Or forgiveness?"`,
      choices: [
        { label: "Demand the vault key", next: "fight" },
        { label: "Confess your debts", next: "blessing" },
        { label: "Steal the key while he speaks", next: "vault" },
      ],
    },

    stranger: {
      title: "A Familiar Face",
      text: `The stranger pulls back their hood. It's your missing sibling—alive, but marked with a cursed sigil.

"They'll hunt us both if you take the gold," they whisper. "Come with me instead."`,
      choices: [
        { label: "Trust your sibling", next: "escape" },
        { label: "Demand the truth", next: "magic" },
        { label: "Turn them in for a reward", next: "betrayal" },
      ],
    },

    fight: {
      title: "Steel and Shadow",
      text: `Blades clash in the dark. You win—but blood is on your hands, and the vault alarm howls through stone corridors.

You grab what you can and run into the night, rich but forever hunted.`,
      choices: [],
    },

    vault: {
      title: "The Golden Hoard",
      text: `The vault door groans open. Gold spills like sunlight. For one breath, you are free.

Then the ceiling cracks. You escape with a single chest—and a story no tavern will believe.`,
      choices: [],
    },

    magic: {
      title: "Arcane Bargain",
      text: `Blue fire coils around your wrist. A voice offers power in exchange for your name.

You accept. The debts vanish. So does your reflection.`,
      choices: [],
    },

    blessing: {
      title: "Mercy",
      text: `The priest places a hand on your brow. Warmth floods your chest. The map crumbles to ash.

You leave Eldermoor with nothing but peace—and for the first time in years, that is enough.`,
      choices: [],
    },

    escape: {
      title: "Together Again",
      text: `You and your sibling vanish into the storm. The vault's curse passes you by.

You may be poor, but you are not alone.`,
      choices: [],
    },

    betrayal: {
      title: "The Price of Gold",
      text: `The reward is paid in coin and silence. Your sibling's eyes meet yours one last time before the guards take them.

You count the gold until dawn, and never sleep again.`,
      choices: [],
    },

    forest: {
        title: "The Whispering Woods",
        text: "Moss glows under ancient trees...",
        choices: [
            { label: "Follow the light", next: "magic" },
            { label: "Turn back", next: "intro" },
            { label: "Call out", next: "fight" },
        ],
    }
  },
};

/* ------------------------------------------------------------------ */
/* Game engine — you usually don't need to edit below this line       */
/* ------------------------------------------------------------------ */

const storyBox = document.getElementById("story-box");
const choicesNav = document.getElementById("choices");
const restartBtn = document.getElementById("restart-btn");

const CHOICE_SLOTS = 3;

function getScene(sceneId) {
  const scene = STORY.scenes[sceneId];
  if (!scene) {
    console.error(`Missing scene: "${sceneId}"`);
    return {
      title: "Lost in the story",
      text: "This path leads nowhere. Check your scene ids in script.js.",
      choices: [{ label: "Restart", next: STORY.startScene }],
    };
  }
  return scene;
}

function renderScene(sceneId) {
  const scene = getScene(sceneId);

  storyBox.innerHTML = `
    ${scene.title ? `<p class="scene-title">${scene.title}</p>` : ""}
    <p>${scene.text.trim().replace(/\n\n/g, "</p><p>")}</p>
  `;

  const choices = scene.choices ?? [];
  choicesNav.innerHTML = "";

  for (let i = 0; i < CHOICE_SLOTS; i += 1) {
    const choice = choices[i];
    const button = document.createElement("button");
    button.type = "button";
    button.className = "choice-btn";

    if (choice) {
      button.textContent = choice.label;
      button.addEventListener("click", () => {
        if (choice.next) {
          renderScene(choice.next);
        } else {
          showEnding(scene);
        }
      });
    } else {
      button.disabled = true;
      button.classList.add("is-hidden");
      button.textContent = "";
    }

    choicesNav.appendChild(button);
  }

  const isEnding = choices.length === 0;
  restartBtn.hidden = !isEnding;
}

function showEnding(scene) {
  storyBox.innerHTML = `
    ${scene.title ? `<p class="scene-title">${scene.title}</p>` : ""}
    <p>${scene.text.trim().replace(/\n\n/g, "</p><p>")}</p>
    <p><em>The End.</em></p>
  `;

  choicesNav.innerHTML = "";
  for (let i = 0; i < CHOICE_SLOTS; i += 1) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "choice-btn is-hidden";
    button.disabled = true;
    choicesNav.appendChild(button);
  }

  restartBtn.hidden = false;
}

restartBtn.addEventListener("click", () => {
  restartBtn.hidden = true;
  renderScene(STORY.startScene);
});

renderScene(STORY.startScene);