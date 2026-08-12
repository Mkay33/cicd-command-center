function EnvironmentStatus() {
  const envs = [
    { name: "DEV", status: "🟢" },
    { name: "QA", status: "🟢" },
    { name: "STAGING", status: "🟡" },
    { name: "PRE-PROD", status: "🔴" },
    { name: "PRODUCTION", status: "🟢" },
  ];

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        marginBottom: "30px",
      }}
    >
      {envs.map((env) => (
        <div key={env.name} style={{ textAlign: "center" }}>
          <h4>{env.name}</h4>
          <h2>{env.status}</h2>
        </div>
      ))}
    </div>
  );
}

export default EnvironmentStatus;