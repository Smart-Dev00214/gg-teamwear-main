import {
  Datagrid,
  DateField,
  ExportButton,
  FilterButton,
  List,
  NumberField,
  SelectField,
  TextField,
  TopToolbar,
} from "react-admin";
import { CourierChoices } from "../values/courier-choices";
import {
  ShipmentStatusChoices,
  ShipmentStatusType,
} from "../values/shipment-status-choices";
import { ShipmentFilters } from "../components/shipment-filters";
import { ShipmentListBulkActionButtons } from "../components/shipment-list-bulk-action-buttons";

export const ShipmentList = () => {
  function isRowSelectable(record) {
    return (
      [ShipmentStatusType.CONFIRMED, ShipmentStatusType.NOTIFIED].includes(
        record.status
      ) && record.courier === "tnt"
    );
  }

  return (
    <List
      actions={
        <TopToolbar>
          <FilterButton />
          <ExportButton />
        </TopToolbar>
      }
      filters={ShipmentFilters}
    >
      <Datagrid
        rowClick="show"
        isRowSelectable={isRowSelectable}
        bulkActionButtons={<ShipmentListBulkActionButtons />}
      >
        <TextField source="id" />
        <SelectField source="status" choices={ShipmentStatusChoices} />
        <NumberField source="charge" />
        <NumberField source="billingWeight" />
        <TextField source="shipmentIdentificationNumber" />
        <SelectField source="courier" choices={CourierChoices} />
        <DateField source="date" showTime />
      </Datagrid>
    </List>
  );
};
