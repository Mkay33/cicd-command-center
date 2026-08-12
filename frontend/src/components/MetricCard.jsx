function MetricCard({ title, value }) {
  return (
    <div className="card shadow">
      <div className="card-body text-center">
        <h5>{title}</h5>
        <h2>{value}</h2>
      </div>
    </div>
  );
}

export default MetricCard;