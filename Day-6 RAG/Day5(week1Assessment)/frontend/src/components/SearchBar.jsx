export default function SearchBar({ query, onChange }) {
  return (
    <input
      type="text"
      placeholder="Search by name or symbol..."
      value={query}
      onChange={(e) => onChange(e.target.value)}
    />
  );
}