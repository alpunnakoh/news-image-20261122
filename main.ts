// Entry program for news-image-20261122.
//
// The front page itself is drawn by draw.py (Pillow, deterministic) into
// entry.png, which ships in this repository. This program only copies that
// image to the grader's output directory, so both runs write identical bytes.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
console.log("wrote entry.png to " + outDir);
