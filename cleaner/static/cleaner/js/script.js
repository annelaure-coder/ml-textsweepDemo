(function () {
    const THEME_KEY = "textsweep-theme";

    function getCookie(name) {
        const cookies = document.cookie ? document.cookie.split(";") : [];
        for (let i = 0; i < cookies.length; i += 1) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                return decodeURIComponent(cookie.slice(name.length + 1));
            }
        }
        return null;
    }

    function applyTheme(theme) {
        document.documentElement.setAttribute("data-theme", theme);
        const toggle = document.getElementById("theme-toggle");
        if (toggle) {
            toggle.textContent = theme === "dark" ? "Light mode" : "Dark mode";
        }
    }

    function initTheme() {
        const saved = localStorage.getItem(THEME_KEY);
        const theme = saved === "dark" || saved === "light" ? saved : "light";
        applyTheme(theme);
        const toggle = document.getElementById("theme-toggle");
        if (!toggle) {
            return;
        }
        toggle.addEventListener("click", function () {
            const next =
                document.documentElement.getAttribute("data-theme") === "dark"
                    ? "light"
                    : "dark";
            localStorage.setItem(THEME_KEY, next);
            applyTheme(next);
        });
    }

    function countWords(text) {
        const trimmed = text.trim();
        return trimmed ? trimmed.split(/\s+/).length : 0;
    }

    function setText(id, value) {
        const el = document.getElementById(id);
        if (el) {
            el.textContent = value;
        }
    }

    function initCleaner() {
        const form = document.getElementById("clean-form");
        const textarea = document.getElementById("id_text");
        if (!form || !textarea) {
            return;
        }

        const liveCount = document.getElementById("live-count");
        const errorEl = document.getElementById("form-error");
        const cleanBtn = document.getElementById("clean-btn");
        const clearBtn = document.getElementById("clear-btn");
        const copyBtn = document.getElementById("copy-btn");
        const copyStatus = document.getElementById("copy-status");
        const results = document.getElementById("results");

        function updateCount() {
            const text = textarea.value;
            liveCount.textContent =
                text.length + " characters · " + countWords(text) + " words";
        }

        function showError(message) {
            errorEl.hidden = false;
            errorEl.textContent = message;
        }

        function clearError() {
            errorEl.hidden = true;
            errorEl.textContent = "";
        }

        function renderResult(data) {
            results.classList.remove("is-empty");
            setText("original-text", data.original);
            setText("cleaned-text", data.cleaned);
            setText("stat-char-before", data.stats.char_count_before);
            setText("stat-char-after", data.stats.char_count_after);
            setText("stat-word-before", data.stats.word_count_before);
            setText("stat-word-after", data.stats.word_count_after);
            copyBtn.disabled = !data.cleaned;
        }

        function resetResults() {
            results.classList.add("is-empty");
            setText("original-text", "");
            setText("cleaned-text", "");
            setText("stat-char-before", "—");
            setText("stat-char-after", "—");
            setText("stat-word-before", "—");
            setText("stat-word-after", "—");
            copyBtn.disabled = true;
            copyStatus.hidden = true;
        }

        textarea.addEventListener("input", updateCount);
        updateCount();

        form.addEventListener("submit", function (event) {
            event.preventDefault();
            clearError();

            const text = textarea.value;
            if (!text.trim()) {
                showError("Please enter some text to clean.");
                return;
            }

            const csrf = getCookie("csrftoken");
            cleanBtn.disabled = true;
            cleanBtn.textContent = "Cleaning…";

            fetch("/api/clean/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrf || "",
                },
                body: JSON.stringify({ text: text }),
            })
                .then(function (response) {
                    return response.json().then(function (data) {
                        return { ok: response.ok, data: data };
                    });
                })
                .then(function (result) {
                    if (!result.ok) {
                        showError(
                            result.data.error ||
                                "Cleaning failed. Please try again."
                        );
                        return;
                    }
                    renderResult(result.data);
                })
                .catch(function () {
                    showError("Could not reach the cleaner. Please try again.");
                })
                .finally(function () {
                    cleanBtn.disabled = false;
                    cleanBtn.textContent = "Clean";
                });
        });

        clearBtn.addEventListener("click", function () {
            textarea.value = "";
            updateCount();
            clearError();
            resetResults();
            textarea.focus();
        });

        copyBtn.addEventListener("click", function () {
            const cleaned = document.getElementById("cleaned-text").textContent;
            if (!cleaned) {
                return;
            }
            navigator.clipboard.writeText(cleaned).then(
                function () {
                    copyStatus.hidden = false;
                    copyStatus.textContent = "Copied to clipboard.";
                },
                function () {
                    copyStatus.hidden = false;
                    copyStatus.textContent = "Could not copy. Select the text instead.";
                }
            );
        });
    }

    initTheme();
    initCleaner();
})();
