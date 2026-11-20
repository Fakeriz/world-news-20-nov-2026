// world-news-20-nov-2026 — make.fun news-image-20261120 entry (Node 22, stdlib only).
// The entry image is entry.png beside this file; the program copies it to
// /output/entry.png (MAKEFUN_OUTPUT_DIR stands in for /output outside the grader).
// Run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = new URL("./entry.png", import.meta.url);
copyFileSync(source, join(outDir, "entry.png"));
