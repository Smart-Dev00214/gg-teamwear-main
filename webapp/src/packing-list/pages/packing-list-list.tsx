import {
  Datagrid,
  DateField,
  List,
  NumberField,
  SelectField,
  TextField,
  useGetOne,
  useRecordSelection,
} from "react-admin";
import {
  PackingListStatusChoices,
  PackingListStatusType,
} from "../values/packing-list-status-choices";
import { PackingListFilters } from "../components/packing-list-filters";
import { PackingListListBulkActionButtons } from "../components/packing-list-list-bulk-action-buttons";

export const PackingListList = () => {
  const [selectedIds] = useRecordSelection("packing-list");
  const { data: firstSelectedRecord } = useGetOne(
    "packing-list",
    {
      id: selectedIds[0],
    },
    { enabled: selectedIds.length > 0 }
  );

  function isRowSelectable(record) {
    return (
      record.status === PackingListStatusType.RECEIVED &&
      (firstSelectedRecord
        ? record.shipToGLN === firstSelectedRecord.shipToGLN
        : true)
    );
  }

  return (
    <List filters={PackingListFilters}>
      <Datagrid
        rowClick="show"
        isRowSelectable={isRowSelectable}
        bulkActionButtons={<PackingListListBulkActionButtons />}
      >
        <TextField source="id" />
        <TextField source="documentNumber" />
        <NumberField source="totalItems" />
        <SelectField source="status" choices={PackingListStatusChoices} />
        <DateField source="receivedDate" />
        <TextField source="shipToGLN" label="Ship to GLN" />
      </Datagrid>
    </List>
  );
};
