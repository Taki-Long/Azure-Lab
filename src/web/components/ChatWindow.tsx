'use client'

import { useState } from 'react';
import { Card, TextArea } from '@radix-ui/themes';
import { Button} from '@radix-ui/themes';


const Chatbot = () => {

  return (
    <div className="flex flex-col h-screen space-y-4 p-8">
      <Card className="grow">
      </Card>
      <div className="flex flex-row items-center space-x-4">
        <div className="grow content-center">
          <TextArea></TextArea>
        </div>
        <Button size="4" className="w-32">Send</Button>
      </div>
    </div>
  );
};

export default Chatbot;
