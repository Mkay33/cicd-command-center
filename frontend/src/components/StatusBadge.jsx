function StatusBadge({ status }) {
  let color = "#6c757d";

  switch (status.toUpperCase()) {
    case "SUCCESS":
      color = "green";
      break;
    case "FAILED":
      color = "red";
      break;
    case "RUNNING":
      color = "orange";
      break;
    default:
      color = "gray";
  }

  return (
    <span
      style={{
        backgroundColor: color,
        color: "white",
        padding: "5px 10px",
        borderRadius: "20px",
        fontWeight: "bold",
      }}
    >
      {status}
    </span>
  );
}

export default StatusBadge;