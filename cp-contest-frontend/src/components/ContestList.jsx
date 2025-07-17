// src/components/ContestList.jsx
import React from "react";
import ContestCard from "./ContestCard";

const ContestList = ({ contests }) => {
  return (
    <ul style={{ listStyle: "none", padding: 0, maxWidth: "700px", margin: "auto" }}>
      {contests.length > 0 ? (
        contests.map((contest, index) => (
          <ContestCard key={index} contest={contest} />
        ))
      ) : (
        <div style={{ textAlign: "center", color: "#888" }}>No contests found.</div>
      )}
    </ul>
  );
};

export default ContestList;
