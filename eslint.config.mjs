import eslint from '@eslint/js';
import { defineConfig, globalIgnores } from 'eslint/config';
import tseslint from 'typescript-eslint';

const ignoreList = [
  "dist/",
  "node_modules/",
  "build/",
];

export default defineConfig(
  eslint.configs.recommended,
  tseslint.configs.recommended,
  [globalIgnores(ignoreList)],
);
