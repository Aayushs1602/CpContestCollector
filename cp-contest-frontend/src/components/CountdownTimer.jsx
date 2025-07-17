// src/components/CountdownTimer.jsx
import React, { useEffect, useState } from "react";

const CountdownTimer = ({ startTime }) => {
  const calculateTimeLeft = () => {
    const now = new Date();
    const difference = new Date(startTime) - now;

    if (difference <= 0) return null;

    const hours = Math.floor(difference / (1000 * 60 * 60));
    const minutes = Math.floor((difference / (1000 * 60)) % 60);
    const seconds = Math.floor((difference / 1000) % 60);

    return `${hours}h ${minutes}m ${seconds}s`;
  };

  const [timeLeft, setTimeLeft] = useState(calculateTimeLeft());

  useEffect(() => {
    const timer = setInterval(() => {
      const newTime = calculateTimeLeft();
      setTimeLeft(newTime);
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  return timeLeft ? (
    <div style={{ marginTop: "0.5rem", color: "#ff9800" }}>
      ⏳ Starts in: <strong>{timeLeft}</strong>
    </div>
  ) : (
    <div style={{ marginTop: "0.5rem", color: "red" }}>🚀 Starting Now!</div>
  );
};

export default CountdownTimer;
