// src/App.jsx
import React, { useEffect, useState } from "react";
import ContestList from "./components/ContestList";

function App() {
  const [contests, setContests] = useState([]);
  const [platformFilter, setPlatformFilter] = useState("All");
  const [sortOrder, setSortOrder] = useState("asc");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/contests/")
      .then((res) => res.json())
      .then((data) => setContests(data))
      .catch((err) => console.error("Error fetching contests:", err));
  }, []);

  const uniquePlatforms = [...new Set(contests.map((c) => c.platform))];

  const filteredContests = contests
    .filter((c) => new Date(c.start_time) > new Date())
    .filter((c) => platformFilter === "All" || c.platform === platformFilter)
    .sort((a, b) => {
      const timeA = new Date(a.start_time);
      const timeB = new Date(b.start_time);
      return sortOrder === "asc" ? timeA - timeB : timeB - timeA;
    });

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif", color: "#111" }}>
      <h1 style={{ fontSize: "2.5rem", marginBottom: "1rem" }}>
        📅 Upcoming CP Contests
      </h1>

      <div style={{ marginBottom: "1rem" }}>
        <label style={{ marginRight: "1rem" }}>Filter by platform:</label>
        <select
          value={platformFilter}
          onChange={(e) => setPlatformFilter(e.target.value)}
        >
          <option value="All">All</option>
          {uniquePlatforms.map((p) => (
            <option key={p} value={p}>
              {p}
            </option>
          ))}
        </select>

        <label style={{ marginLeft: "2rem", marginRight: "1rem" }}>
          Sort by time:
        </label>
        <select
          value={sortOrder}
          onChange={(e) => setSortOrder(e.target.value)}
        >
          <option value="asc">Earliest First</option>
          <option value="desc">Latest First</option>
        </select>
      </div>

      {filteredContests.length === 0 ? (
        <p>No upcoming contests found.</p>
      ) : (
        <ContestList contests={filteredContests} />
      )}
    </div>
  );
}

export default App;
