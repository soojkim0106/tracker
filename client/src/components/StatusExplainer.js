import "../css/StatusExplainer.css";

const StatusExplainer = () => {
  return (
    <footer className="status-footer">
      {/* <h3>Color Directory</h3> */}
      <div className="item-box">
        <p className="red">
        Not Started
        </p>
        <p className="yellow">
          In Progress
        </p>
        <p className="green">
          Completed
        </p>
      </div>
    </footer>
  );
};

export default StatusExplainer;