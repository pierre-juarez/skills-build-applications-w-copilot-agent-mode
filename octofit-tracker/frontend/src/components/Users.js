import React, { useEffect, useState } from 'react';

function Users() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState(null);

  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
  console.log('[Users] endpoint:', endpoint);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(endpoint);
        const data = await res.json();
        console.log('[Users] raw data:', data);
        const results = Array.isArray(data) ? data : data?.results ?? [];
        console.log('[Users] items:', results);
        setItems(results);
      } catch (err) {
        console.error('[Users] fetch error:', err);
        setItems([]);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [endpoint]);

  if (loading) return <div>Loading users...</div>;

  return (
    <div>
      <h3 className="h3 mb-3">Users</h3>

      {items.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead>
              <tr>
                <th>#</th>
                <th>ID</th>
                <th>Summary</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {items.map((it, idx) => (
                <tr key={it.id ?? idx}>
                  <td>{idx + 1}</td>
                  <td>{it.id ?? '-'}</td>
                  <td style={{maxWidth: '40ch', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>{JSON.stringify(it)}</td>
                  <td>
                    <button className="btn btn-sm btn-primary me-2" onClick={() => setSelected(it)}>View</button>
                    <a className="btn btn-sm btn-link" href={endpoint + (it.id ?? '')}>API</a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {selected && (
        <div className="modal show d-block" tabIndex="-1">
          <div className="modal-dialog modal-lg">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">User Details</h5>
                <button type="button" className="btn-close" aria-label="Close" onClick={() => setSelected(null)} />
              </div>
              <div className="modal-body">
                <pre style={{whiteSpace: 'pre-wrap'}}>{JSON.stringify(selected, null, 2)}</pre>
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" onClick={() => setSelected(null)}>Close</button>
              </div>
            </div>
          </div>
          <div className="modal-backdrop show" />
        </div>
      )}
    </div>
  );
}

export default Users;
