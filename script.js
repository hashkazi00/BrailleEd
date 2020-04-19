/*document.addEventListener("DOMContentLoaded", () => {
  "use.strict";
  console.log("content loaded");
  document.addEventListener("keydown", (event) => {
    const key = event.key.toLowerCase();
    console.log(key);
  });
});*/

var synthesis = undefined;
var voice = undefined;

window.onload = function () {
  var voiceElement = document.getElementById("myBtn");
  // voiceElement.speak();
};

if ("speechSynthesis" in window) {
  synthesis = window.speechSynthesis;
  console.log("1");
  // Regex to match all English language tags e.g en, en-US, en-GB
  var langRegex = /^en(-[a-z]{2})?$/i;
  console.log("2");
  setTimeout(function () {
    // Get the available voices and filter the list to only have English speakers
    voice = synthesis.getVoices().filter(function (voice) {
      return voice.uri === "Rishi";
    })[0];

    speakWord("welcome to digi vision");

    // var voices = synthesis
    //   .getVoices()
    //   .filter((voice) => langRegex.test(voice.lang));

    // Log the properties of the voices in the list
    // voices.forEach(function (voice) {
    //   console.log({
    //     name: voice.name,
    //     lang: voice.lang,
    //     uri: voice.voiceURI,
    //     local: voice.localService,
    //     default: voice.default,
    //   });
    // });
  }, 300);
  console.log("3");
} else {
  console.log("Text-to-speech not supported.");
}

function speakWord(text) {
  var utterance = new SpeechSynthesisUtterance(text);

  // Set utterance properties
  utterance.voice = voice;
  utterance.pitch = 1.6;
  utterance.rate = 1;
  utterance.volume = 1.6;
  console.log("4");
  // Speak the utterance
  synthesis.speak(utterance);
}
