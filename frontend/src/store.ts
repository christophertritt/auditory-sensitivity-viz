import create from 'zustand';

interface AppState {
  scenario: string;
  setScenario: (scenario: string) => void;
  showUrbanNoise: boolean;
  setShowUrbanNoise: (show: boolean) => void;
}

export const useAppStore = create<AppState>((set) => ({
  scenario: 'peak_shipping',
  setScenario: (scenario) => set({ scenario }),
  showUrbanNoise: true,
  setShowUrbanNoise: (show) => set({ showUrbanNoise: show }),
}));
