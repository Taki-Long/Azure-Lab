'use client'
import 'reactflow/dist/style.css';
import { useCallback, useState } from 'react';
import React from 'react';
import ReactFlow, { Background, Connection, Controls, Edge, MiniMap, addEdge, useEdgesState, useNodesState } from 'reactflow';
import { Card } from '@radix-ui/themes';
import LocalCSVFile from './Tasks/LocalCSVFile';

const initialNodes = [
  { id: '1', type: 'localfile', position: { x: 0, y: 0 }, data: { label: '1' } },
  { id: '2', position: { x: 0, y: 100 }, data: { label: '2' } },
];
const initialEdges = [{ id: 'e1-2', source: '1', target: '2' }];

const Workflow = () => {

  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const nodeTypes = { localfile: LocalCSVFile };

  const onConnect = useCallback((params: Edge | Connection) => setEdges((eds) => addEdge(params, eds)), [setEdges]);
  return (
    <div className="flex h-screen space-x-4 p-8">
      <div className="w-64 bg-slate-600">
      </div>
      <div className="grow">
        <ReactFlow
          nodes={nodes}
          edges={edges}
          nodeTypes={nodeTypes}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          fitView >
          <MiniMap zoomable pannable />
          <Background />
          <Controls />
        </ReactFlow>
      </div>
    </div>
  );
};

export default Workflow;
