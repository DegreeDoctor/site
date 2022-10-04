/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution");

module.exports = {
    root: true,
    extends: [
        "plugin:vue/vue3-essential",
        "plugin:vue/vue3-strongly-recommended",
        "plugin:vue/vue3-recommended",
        "eslint:recommended",
        "@vue/eslint-config-prettier",
    ],
    parserOptions: {
        ecmaVersion: "latest",
    },
    rules: {
        "no-unused-vars": "warn",
        "vue/no-unused-vars": "warn",

        "vue/html-indent": ["warn", 4],
        indent: ["warn", 4],
        "prettier/prettier": "off",
        "vue/max-attributes-per-line": [
            "warn",
            {
                singleline: 4,
                multiline: 4,
            },
        ],
    },
};
