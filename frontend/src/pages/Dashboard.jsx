import { useEffect, useState } from "react";
import api from "../services/api";
import Header from "../components/Header";
import EnvironmentStatus from "../components/EnvironmentStatus";
import PipelineTable from "../components/PipelineTable";

function MetricCard({ title, value }) {
  return (
    <div className="card shadow-sm p-3">
      <h6 className="text-muted">{title}</h6>
      <h2>{value}</h2>
    </div>
  );
}

function Dashboard() {
  const [metrics, setMetrics] = useState({
    total_builds: 0,
    successful_builds: 0,
    failed_builds: 0,
    running_builds: 0,
    failure_rate: 0,
    average_build_duration_seconds: 0,
    deployments_today: 0,
  });

  const [pipelines, setPipelines] = useState([]);

  useEffect(() => {
    api
      .get("metrics/")
      .then((response) => {
        console.log("Metrics:", response.data);
        setMetrics(response.data);
      })
      .catch((error) => {
        console.error("Metrics API Error:", error);
      });

    api
      .get("pipelines/")
      .then((response) => {
        console.log("Pipelines:", response.data);
        setPipelines(response.data);
      })
      .catch((error) => {
        console.error("Pipeline API Error:", error);
      });
  }, []);

  return (
    <div className="container mt-4">

      <Header />

      <EnvironmentStatus />

      <h3 className="mt-4 mb-3">Build Metrics</h3>

      <div className="row g-3">

        <div className="col-md-3">
          <MetricCard
            title="Total Builds"
            value={metrics.total_builds}
          />
        </div>

        <div className="col-md-3">
          <MetricCard
            title="Successful"
            value={metrics.successful_builds}
          />
        </div>

        <div className="col-md-3">
          <MetricCard
            title="Failed"
            value={metrics.failed_builds}
          />
        </div>

        <div className="col-md-3">
          <MetricCard
            title="Running"
            value={metrics.running_builds}
          />
        </div>

        <div className="col-md-4">
          <MetricCard
            title="Failure Rate"
            value={`${metrics.failure_rate}%`}
          />
        </div>

        <div className="col-md-4">
          <MetricCard
            title="Average Build Duration"
            value={`${metrics.average_build_duration_seconds}s`}
          />
        </div>

        <div className="col-md-4">
          <MetricCard
            title="Deployments Today"
            value={metrics.deployments_today}
          />
        </div>

      </div>

      <div className="mt-5">
        <PipelineTable pipelines={pipelines} />
      </div>

    </div>
  );
}

export default Dashboard;
