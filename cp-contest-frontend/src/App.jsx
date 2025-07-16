import { useEffect, useState } from "react";

// 🛠️ Helper to generate Google Calendar event link
function generateGoogleCalendarLink(contest) {
  const start = new Date(contest.start_time);
  const end = new Date(start.getTime() + contest.duration * 60000);

  const formatDate = (date) =>
    date.toISOString().replace(/[-:]|\.\d{3}/g, "").slice(0, 15);

  const url = new URL("https://calendar.google.com/calendar/render");
  url.searchParams.set("action", "TEMPLATE");
  url.searchParams.set("text", contest.title);
  url.searchParams.set("dates", `${formatDate(start)}/${formatDate(end)}`);
  url.searchParams.set("details", `Contest on ${contest.platform}`);
  url.searchParams.set("location", "https://codeforces.com/contests");
  url.searchParams.set("sf", "true");
  url.searchParams.set("output", "xml");

  return url.toString();
}

function App() {
  const [contests, setContests] = useState([]);
  const [filteredContests, setFilteredContests] = useState([]);
  const [platformFilter, setPlatformFilter] = useState("All");
  const [sortOrder, setSortOrder] = useState("asc");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/contests/")
      .then((res) => res.json())
      .then((data) => setContests(data))
      .catch((err) => console.error("Error fetching contests:", err));
  }, []);

  useEffect(() => {
    const now = new Date();

    let upcoming = contests.filter((c) => new Date(c.start_time) > now);

    if (platformFilter !== "All") {
      upcoming = upcoming.filter((c) => c.platform === platformFilter);
    }

    upcoming.sort((a, b) => {
      const timeA = new Date(a.start_time);
      const timeB = new Date(b.start_time);
      return sortOrder === "asc" ? timeA - timeB : timeB - timeA;
    });

    setFilteredContests(upcoming);
  }, [contests, platformFilter, sortOrder]);

  const uniquePlatforms = [...new Set(contests.map((c) => c.platform))];

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
        <ul style={{ listStyle: "none", padding: 0 }}>
          {filteredContests.map((contest) => {
            const startTime = new Date(contest.start_time);
            const today = new Date();
            const isToday =
              startTime.getDate() === today.getDate() &&
              startTime.getMonth() === today.getMonth() &&
              startTime.getFullYear() === today.getFullYear();

            return (
              <li
                key={contest.id}
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
                {/* <br /> */}
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
            
          })}
        </ul>
      )}
    </div>
  );
}

export default App;
