import React, { useRef, useState ,useEffect } from "react";
// import ReactPlayer from "react-player/youtube";

const YouTubePlayer = () => {
  const playerRef = useRef(null);
const iframeRef = useRef(null);
const [player, setPlayer] = useState(null);
const [playing, setPlaying] = useState(false);
const [speed, setSpeed] = useState(1);
const [quality, setQuality] = useState("default");

// Load YouTube IFrame API
useEffect(() => {
  const tag = document.createElement("script");
  tag.src = "https://www.youtube.com/iframe_api";
  document.body.appendChild(tag);

  window.onYouTubeIframeAPIReady = () => {
    const newPlayer = new window.YT.Player(iframeRef.current, {
      height: "360",
      width: "640",
      videoId: "dQw4w9WgXcQ", // Replace with your video ID
      playerVars: {
        controls: 0,
        modestbranding: 1,
        rel: 0,
      },
      events: {
        onReady: (e) => {
          setPlayer(e.target);
        },
      },
    });
  };
}, []);

const togglePlay = () => {
  if (player) {
    if (playing) {
      player.pauseVideo();
    } else {
      player.playVideo();
    }
    setPlaying(!playing);
  }
};

const seekBy = (seconds) => {
  if (player) {
    const currentTime = player.getCurrentTime();
    player.seekTo(currentTime + seconds, true);
  }
};

const changeSpeed = (s) => {
  if (player) {
    player.setPlaybackRate(s);
    setSpeed(s);
  }
};

const changeQuality = (q) => {
  if (player) {
    player.setPlaybackQuality(q);
    setQuality(q);
  }
};

return (
  <div className="p-4 max-w-3xl mx-auto space-y-4">
    <div ref={iframeRef} />

    <div className="flex gap-4 items-center justify-center mt-4">
      <button onClick={() => seekBy(-10)} className="px-4 py-2 bg-gray-200 rounded">
        ⏪ 10s
      </button>
      <button onClick={togglePlay} className="px-4 py-2 bg-blue-500 text-white rounded">
        {playing ? "Pause ⏸" : "Play ▶️"}
      </button>
      <button onClick={() => seekBy(10)} className="px-4 py-2 bg-gray-200 rounded">
        10s ⏩
      </button>
    </div>

    <div className="flex items-center gap-2">
      <span>Speed:</span>
      <select
        value={speed}
        onChange={(e) => changeSpeed(parseFloat(e.target.value))}
        className="border rounded px-2 py-1"
      >
        {[0.25, 0.5, 1, 1.25, 1.5, 2].map((s) => (
          <option key={s} value={s}>
            {s}x
          </option>
        ))}
      </select>
    </div>

    <div className="flex items-center gap-2">
      <span>Quality:</span>
      <select
        value={quality}
        onChange={(e) => changeQuality(e.target.value)}
        className="border rounded px-2 py-1"
      >
        <option value="default">Auto</option>
        <option value="highres">Highres</option>
        <option value="hd1080">1080p</option>
        <option value="hd720">720p</option>
        <option value="large">480p</option>
        <option value="medium">360p</option>
        <option value="small">240p</option>
        <option value="tiny">144p</option>
      </select>
    </div>
  </div>
);
};

export default YouTubePlayer;
