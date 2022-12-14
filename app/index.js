function showInfo() {
    const info = document.getElementById("info");
    const model = document.getElementById("model");
    info.classList.remove("hidden");
    model.classList.add("hidden");

    const infoMenu = document.getElementById("info-menu");
    const modelMenu = document.getElementById("model-menu");
    infoMenu.classList = "text-center block border border-blue-500 rounded py-2 px-4 bg-blue-500 hover:bg-blue-700 text-white"
    modelMenu.classList = "text-center block border border-white rounded hover:border-gray-200 text-blue-500 hover:bg-gray-200 py-2 px-4"
}

function showModel() {
    const info = document.getElementById("info");
    const model = document.getElementById("model");
    model.classList.remove("hidden");
    info.classList.add("hidden");

    const infoMenu = document.getElementById("info-menu");
    const modelMenu = document.getElementById("model-menu");
    infoMenu.classList = "text-center block border border-white rounded hover:border-gray-200 text-blue-500 hover:bg-gray-200 py-2 px-4"
    modelMenu.classList = "text-center block border border-blue-500 rounded py-2 px-4 bg-blue-500 hover:bg-blue-700 text-white"
}

