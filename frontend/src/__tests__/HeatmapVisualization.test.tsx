import React from 'react';
import { render, screen } from '@testing-library/react';
import HeatmapVisualization from '../components/HeatmapVisualization';

test('renders HeatmapVisualization loading state', () => {
  render(<HeatmapVisualization />);
  expect(screen.getByText(/Loading heatmap/i)).toBeInTheDocument();
});
