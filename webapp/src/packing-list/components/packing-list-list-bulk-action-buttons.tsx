import { useListContext } from "react-admin";
import { Button } from "@mui/material";
import { Link } from "react-router-dom";

export function PackingListListBulkActionButtons() {
  const { selectedIds } = useListContext();

  return (
    <>
      <Button
        component={Link}
        to={{ pathname: "/shipment/create" }}
        state={{ record: { packingLists: selectedIds } }}
      >
        Create shipment
      </Button>
    </>
  );
}
