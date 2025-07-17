// src/components/ContestCard.jsx
import React from "react";
import CountdownTimer from "./CountdownTimer";
import { generateGoogleCalendarLink } from "../utils/calendarUtils";

const ContestCard = ({ contest }) => {
  const startTime = new Date(contest.start_time);
  const today = new Date();
  const isToday =
    startTime.getDate() === today.getDate() &&
    startTime.getMonth() === today.getMonth() &&
    startTime.getFullYear() === today.getFullYear();

  return (
    <li
      style={{
        marginBottom: "1rem",
        padding: "1rem",
        backgroundColor: isToday ? "#e6ffe6" : "#ffffff",
        border: isToday ? "2px solid green" : "1px solid #ccc",
        borderRadius: "8px",
        color: "#111",
        boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
      }}
    >
      <strong>{contest.title}</strong> — {contest.platform}
      <br />
      <span role="img" aria-label="clock">
        ⏰
      </span>{" "}
      Start: {startTime.toLocaleString()}
      <br />
      <span role="img" aria-label="duration">
        🕒
      </span>{" "}
      Duration: {contest.duration} minutes
      <CountdownTimer startTime={contest.start_time} />
      {isToday && (
        <div
          style={{
            color: "green",
            fontWeight: "bold",
            marginTop: "0.5rem",
          }}
        >
          🚀 Happening Today!
        </div>
      )}
      <br />
      <a
        href={generateGoogleCalendarLink(contest)}
        target="_blank"
        rel="noopener noreferrer"
        style={{
          display: "inline-block",
          marginTop: "0.5rem",
          padding: "0.3rem 0.6rem",
          backgroundColor: "#4285F4",
          color: "#fff",
          borderRadius: "4px",
          textDecoration: "none",
          fontSize: "0.9rem",
        }}
      >
        ➕ Add to Google Calendar
      </a>
      <a
        href={contest.url}
        target="_blank"
        rel="noopener noreferrer"
        style={{
          display: "inline-block",
          marginTop: "0.5rem",
          marginLeft: "0.5rem",
          padding: "0.3rem 0.6rem",
          backgroundColor: "#00C853",
          color: "#fff",
          borderRadius: "4px",
          textDecoration: "none",
          fontSize: "0.9rem",
        }}
      >
        🔗 Visit Contest Page
      </a>
    </li>
  );
};

export default ContestCard;
