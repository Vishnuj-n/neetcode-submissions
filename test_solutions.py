#!/usr/bin/env python3
"""
Basic testing framework for validating NeetCode solutions.
Run with: python test_solutions.py [--problem PROBLEM_NAME] [--verbose]
"""

import sys
import ast
import importlib.util
import traceback
from pathlib import Path
from typing import List, Dict, Any, Optional
import argparse

class SolutionValidator:
    def __init__(self, data_root: Path = Path("./Data Structures & Algorithms")):
        self.data_root = data_root
        self.errors = []
        self.warnings = []
        
    def validate_syntax(self, file_path: Path) -> bool:
        """Check if Python file has valid syntax."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
            return True
        except SyntaxError as e:
            self.errors.append(f"Syntax error in {file_path.name}: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading {file_path.name}: {e}")
            return False
    
    def validate_structure(self, file_path: Path) -> bool:
        """Check if file contains required Solution class and methods."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content)
            has_solution_class = False
            has_methods = False
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name == "Solution":
                    has_solution_class = True
                    # Check for at least one method
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            has_methods = True
                            break
            
            if not has_solution_class:
                self.warnings.append(f"No Solution class found in {file_path.name}")
            elif not has_methods:
                self.warnings.append(f"Solution class has no methods in {file_path.name}")
            
            return has_solution_class and has_methods
        except Exception as e:
            self.errors.append(f"Structure validation failed for {file_path.name}: {e}")
            return False
    
    def load_module(self, file_path: Path):
        """Load Python file as module."""
        spec = importlib.util.spec_from_file_location("solution_module", file_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load spec for {file_path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    
    def test_instantiation(self, file_path: Path) -> bool:
        """Test if Solution class can be instantiated."""
        try:
            module = self.load_module(file_path)
            if hasattr(module, 'Solution'):
                solution = module.Solution()
                return True
            else:
                self.warnings.append(f"No Solution class to instantiate in {file_path.name}")
                return False
        except Exception as e:
            self.errors.append(f"Failed to instantiate Solution in {file_path.name}: {e}")
            return False
    
    def validate_file(self, file_path: Path) -> Dict[str, bool]:
        """Run all validation checks on a single file."""
        results = {
            'syntax': self.validate_syntax(file_path),
            'structure': self.validate_structure(file_path),
            'instantiation': False
        }
        
        # Only test instantiation if syntax is valid
        if results['syntax']:
            results['instantiation'] = self.test_instantiation(file_path)
        
        return results
    
    def validate_problem(self, problem_name: str) -> Dict[str, Any]:
        """Validate all submissions for a specific problem."""
        problem_dir = self.data_root / problem_name
        if not problem_dir.exists():
            self.errors.append(f"Problem directory not found: {problem_name}")
            return {'valid': False, 'submissions': []}
        
        py_files = list(problem_dir.glob("submission-*.py"))
        if not py_files:
            self.warnings.append(f"No Python submissions found for {problem_name}")
            return {'valid': True, 'submissions': []}
        
        submission_results = []
        for file_path in sorted(py_files):
            results = self.validate_file(file_path)
            submission_results.append({
                'file': file_path.name,
                'results': results
            })
        
        # Problem is valid if at least one submission passes all checks
        valid = any(all(r['results'].values()) for r in submission_results)
        
        return {
            'valid': valid,
            'submissions': submission_results
        }
    
    def validate_all(self) -> Dict[str, Any]:
        """Validate all problems in the data directory."""
        if not self.data_root.exists():
            self.errors.append(f"Data directory not found: {self.data_root}")
            return {'valid': False, 'problems': {}}
        
        problem_dirs = [d for d in self.data_root.iterdir() if d.is_dir()]
        results = {}
        
        for problem_dir in sorted(problem_dirs):
            problem_name = problem_dir.name
            results[problem_name] = self.validate_problem(problem_name)
        
        total_problems = len(results)
        valid_problems = sum(1 for r in results.values() if r['valid'])
        
        return {
            'valid': valid_problems == total_problems,
            'total_problems': total_problems,
            'valid_problems': valid_problems,
            'problems': results
        }

def main():
    parser = argparse.ArgumentParser(description='Validate NeetCode solutions')
    parser.add_argument('--problem', help='Validate specific problem only')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    args = parser.parse_args()
    
    validator = SolutionValidator()
    
    if args.problem:
        results = validator.validate_problem(args.problem)
        print(f"\nProblem: {args.problem}")
        print(f"Valid: {results['valid']}")
        
        if args.verbose:
            for submission in results['submissions']:
                print(f"  {submission['file']}: {submission['results']}")
    else:
        results = validator.validate_all()
        print(f"\nValidation Summary:")
        print(f"Total problems: {results['total_problems']}")
        print(f"Valid problems: {results['valid_problems']}")
        print(f"Overall valid: {results['valid']}")
        
        if args.verbose:
            for problem_name, problem_result in results['problems'].items():
                status = "✓" if problem_result['valid'] else "✗"
                print(f"\n{status} {problem_name}")
                for submission in problem_result['submissions']:
                    file_status = "✓" if all(submission['results'].values()) else "✗"
                    print(f"  {file_status} {submission['file']}")
                    if args.verbose and not all(submission['results'].values()):
                        for check, passed in submission['results'].items():
                            if not passed:
                                print(f"    - {check}: FAILED")
    
    if validator.errors:
        print(f"\nErrors ({len(validator.errors)}):")
        for error in validator.errors:
            print(f"  - {error}")
    
    if validator.warnings:
        print(f"\nWarnings ({len(validator.warnings)}):")
        for warning in validator.warnings:
            print(f"  - {warning}")
    
    return 0 if results['valid'] else 1

if __name__ == "__main__":
    sys.exit(main())
