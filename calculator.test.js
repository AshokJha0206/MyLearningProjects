import { describe, it, expect } from 'vitest';
import { Calculator } from './calculator.js';

describe('Calculator', () => {
  const calculator = new Calculator();

  it('adds two numbers', () => {
    expect(calculator.add(2, 3)).toBe(5);
  });

  it('adds negative numbers correctly', () => {
    expect(calculator.add(-4, -6)).toBe(-10);
  });

  it('adds decimals correctly', () => {
    expect(calculator.add(1.5, 2.25)).toBeCloseTo(3.75);
  });

  it('subtracts two numbers', () => {
    expect(calculator.subtract(10, 4)).toBe(6);
  });

  it('multiplies two numbers', () => {
    expect(calculator.multiply(3, 5)).toBe(15);
  });

  it('divides two numbers', () => {
    expect(calculator.divide(10, 2)).toBe(5);
  });

  it('throws when dividing by zero', () => {
    expect(() => calculator.divide(5, 0)).toThrow('Cannot divide by zero');
  });
});
