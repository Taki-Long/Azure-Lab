import { Handle, Position } from 'reactflow';

const LocalCSVFile = () => {

  return (
    <div className="w-32 border-solid border-2 border-indigo-600 rounded text-center">
        <div>
          Local CSV File
        </div>
        <Handle type="source" position={Position.Bottom} id="a" />
    </div>
  );
}

export default LocalCSVFile