'use client'

import { useState } from 'react';
import { TextArea } from '@radix-ui/themes';
import { Flex, Button, Box, Container } from '@radix-ui/themes';

const Chatbot = () => {
  return (
    <Flex direction="column" gap="3">
      <Container className="h-[90vh] bg-slate-200">
      </Container>
      <Flex gap="3">
        <Box width="100%">
          <TextArea placeholder="Reply to comment…" />
        </Box>
        <Box height="100%">
          <Button m="2" size="4">Send
          </Button>
        </Box>
      </Flex>
    </Flex>
  );
};

export default Chatbot;
