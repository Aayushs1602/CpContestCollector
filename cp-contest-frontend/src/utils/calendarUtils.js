// src/utils/calendarUtils.js
export function generateGoogleCalendarLink(contest) {
  const start = new Date(contest.start_time);
  const end = new Date(start.getTime() + contest.duration * 60000);

  const formatDate = (date) =>
    date.toISOString().replace(/[-:]|\.\d{3}/g, "").slice(0, 15);

  const url = new URL("https://calendar.google.com/calendar/render");
  url.searchParams.set("action", "TEMPLATE");
  url.searchParams.set("text", contest.title);
  url.searchParams.set("dates", `${formatDate(start)}/${formatDate(end)}`);
  url.searchParams.set("details", `Contest on ${contest.platform}`);
  url.searchParams.set("location", contest.url || "https://example.com");
  url.searchParams.set("sf", "true");
  url.searchParams.set("output", "xml");

  return url.toString();
}
