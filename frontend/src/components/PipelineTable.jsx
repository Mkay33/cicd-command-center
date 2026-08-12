function PipelineTable({ pipelines }) {
  return (
    <div style={{ marginTop: "30px" }}>
      <h2>Pipeline Runs</h2>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "15px",
        }}
      >
        <thead>
          <tr>
            <th>Environment</th>
            <th>Pipeline</th>
            <th>Provider</th>
            <th>Status</th>
            <th>Branch</th>
            <th>Triggered By</th>
          </tr>
        </thead>

        <tbody>
          {pipelines.length === 0 ? (
            <tr>
              <td colSpan="6" style={{ textAlign: "center", padding: "20px" }}>
                No pipeline runs found.
              </td>
            </tr>
          ) : (
            pipelines.map((pipeline) => (
              <tr key={pipeline.id}>
                <td>{pipeline.environment}</td>
                <td>{pipeline.pipeline_name}</td>
                <td>{pipeline.ci_provider}</td>
                <td>{pipeline.status}</td>
                <td>{pipeline.branch}</td>
                <td>{pipeline.triggered_by}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

export default PipelineTable;


