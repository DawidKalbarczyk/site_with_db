const apiBaseUrlInput = document.getElementById("apiBaseUrl");
const itemIdInput = document.getElementById("itemId");
const itemQInput = document.getElementById("itemQ");
const sendBtn = document.getElementById("sendBtn");
const resultEl = document.getElementById("result");

async function sendItemRequest() {
	const apiBaseUrl = apiBaseUrlInput.value.trim().replace(/\/$/, "");
	const itemId = Number(itemIdInput.value);
	const q = itemQInput.value.trim();

	if (!apiBaseUrl) {
		resultEl.textContent = "Podaj API base URL.";
		return;
	}

	if (!Number.isInteger(itemId) || itemId <= 0) {
		resultEl.textContent = "item_id musi byc dodatnia liczba calkowita.";
		return;
	}

	const url = new URL(`${apiBaseUrl}/items/${itemId}`);
	if (q) {
		url.searchParams.set("q", q);
	}

	resultEl.textContent = "Wysylanie...";

	try {
		const response = await fetch(url.toString(), {
			method: "GET",
			headers: {
				"Accept": "application/json"
			}
		});

		if (!response.ok) {
			throw new Error(`HTTP ${response.status} ${response.statusText}`);
		}

		const data = await response.json();
		resultEl.textContent = JSON.stringify(data, null, 2);
	} catch (error) {
		resultEl.textContent = `Blad: ${error.message}`;
	}
}

sendBtn.addEventListener("click", sendItemRequest);
